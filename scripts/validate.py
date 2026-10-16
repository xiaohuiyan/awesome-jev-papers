"""Offline validation of metadata, provenance, bilingual output and links."""
from __future__ import annotations

import datetime as dt
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlparse

from render import ROOT, load, outputs


def validate(data):
    errors = []
    def require(condition, message):
        if not condition:
            errors.append(message)

    papers = data["papers"]
    ids = [p["arxiv_id"] for p in papers]
    require(len(ids) == len(set(ids)), "Duplicate arXiv IDs")
    titles = [re.sub(r"\W+", "", p["title"]).casefold() for p in papers]
    require(len(titles) == len(set(titles)), "Duplicate normalized titles")
    require(len(data["recommended"]) <= 10, "More than ten recommended papers")
    require(len(data["recommended"]) == len(set(data["recommended"])), "Repeated recommendation")
    require(set(data["recommended"]) <= set(ids), "Recommendation references missing paper")
    for p in papers:
        pid = p["arxiv_id"]
        require(bool(re.fullmatch(r"\d{4}\.\d{4,5}", pid)), f"{pid}: invalid arXiv ID")
        require(isinstance(p["version"], int) and p["version"] >= 1, f"{pid}: invalid version")
        require(p["primary_category"] in data["categories"], f"{pid}: unknown category")
        require(p["relation_level"] in {"direct", "related", "background"}, f"{pid}: unknown relation")
        require(bool(p["authors"]) and all(p["authors"]), f"{pid}: missing authors")
        for date_key in ("first_submitted", "updated", "verified_on"):
            try:
                dt.date.fromisoformat(p[date_key])
            except (ValueError, TypeError):
                errors.append(f"{pid}: invalid {date_key}")
        require(p["first_submitted"] <= p["updated"] <= p["verified_on"] <= data["updated_on"], f"{pid}: inconsistent dates")
        if p["relation_level"] != "background":
            require(data["window"]["start"] <= p["first_submitted"] <= data["window"]["end"], f"{pid}: outside main window")
        require(p["reviewed_url"] == f"https://arxiv.org/abs/{pid}v{p['version']}", f"{pid}: wrong reviewed URL")
        require(p["pdf_url"] == f"https://arxiv.org/pdf/{pid}v{p['version']}", f"{pid}: wrong PDF URL")
        for lang in ("en", "zh"):
            require(bool(p["summary"].get(lang)) and bool(p["relation"].get(lang)), f"{pid}: missing {lang} annotation")
        require(bool(re.search(r"[\u4e00-\u9fff]", p["summary"]["zh"])), f"{pid}: Chinese summary missing")
        require(p["tags"] and len(p["tags"]) == len(set(p["tags"])), f"{pid}: invalid tags")
        require({e["criterion"] for e in p["evidence"]} == set(data["relevance_weights"]), f"{pid}: missing criterion evidence")
        require(sum(len(e["quote"].split()) for e in p["evidence"]) <= 25, f"{pid}: excessive quotation")
        for e in p["evidence"]:
            require(0 < len(e["quote"]) <= 80 and bool(e["location"]), f"{pid}: invalid evidence excerpt")
            require(e["source_url"] in {p["reviewed_url"], f"https://arxiv.org/html/{pid}v{p['version']}"}, f"{pid}: evidence source mismatch")
        scores = p["relevance"]["scores"]
        require(all(0 <= x <= 1 for x in scores.values()), f"{pid}: invalid score")
        expected = round(sum(scores[k] * w for k, w in data["relevance_weights"].items()), 2)
        require(expected == p["relevance"]["weighted_total"], f"{pid}: relevance score arithmetic")
        require(p["relation_level"] == "background" or expected >= 0.7, f"{pid}: below main inclusion threshold")
        for c in p["code"]:
            require(c["url"].startswith("https://github.com/") and c["source_url"].startswith("https://arxiv.org/"), f"{pid}: invalid code provenance")
            require(c["verified_on"] <= data["updated_on"] and bool(c["source_location"]), f"{pid}: code unverified")
    return errors


def check_markdown_links():
    errors = []
    for path in ROOT.rglob("*.md"):
        if any(x in path.parts for x in (".git", ".cache")):
            continue
        text = path.read_text(encoding="utf-8")
        # Repository documents use explicit ASCII IDs for stable bilingual anchors.
        for target in re.findall(r"\]\(([^)]+)\)", text):
            if urlparse(target).scheme:
                continue
            filepart, _, anchor = target.partition("#")
            dest = (path.parent / unquote(filepart)).resolve() if filepart else path
            if not dest.exists():
                errors.append(f"{path.relative_to(ROOT)}: missing link {target}")
            elif anchor and f'id="{unquote(anchor)}"' not in dest.read_text(encoding="utf-8"):
                errors.append(f"{path.relative_to(ROOT)}: missing explicit anchor {target}")
    return errors


def main():
    data = load()
    errors = validate(data)
    for name, content in outputs(data).items():
        path = ROOT / name
        if not path.exists() or path.read_text(encoding="utf-8") != content:
            errors.append("Generated output stale: " + name)
    errors += check_markdown_links()
    screening = json.loads((ROOT / "data/screening.json").read_text(encoding="utf-8"))["candidates"]
    log = json.loads((ROOT / "data/search-log.json").read_text(encoding="utf-8"))
    if len(screening) != log["unique_candidates"] or len({s["arxiv_id"] for s in screening}) != len(screening):
        errors.append("Screening ledger count or uniqueness mismatch")
    if {s["arxiv_id"] for s in screening if s["status"] == "included"} != {p["arxiv_id"] for p in data["papers"]}:
        errors.append("Screening ledger does not match included papers")
    for status in ("included", "excluded", "pending"):
        if sum(s["status"] == status for s in screening) != log["outcomes"].get(status, 0):
            errors.append("Screening outcome count mismatch: " + status)
    code_checks = json.loads((ROOT / "data/code-checks.json").read_text(encoding="utf-8"))
    verified = {(c["arxiv_id"], c["canonical_url"]) for c in code_checks if c["status"] == "verified" and not c["private"]}
    for p in data["papers"]:
        for code in p["code"]:
            if (p["arxiv_id"], code["url"]) not in verified:
                errors.append("Code link missing a public repository check: " + p["arxiv_id"])
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"PASS: {len(data['papers'])} papers; bilingual output, BibTeX, evidence, screening and internal links are consistent.")


if __name__ == "__main__":
    main()
