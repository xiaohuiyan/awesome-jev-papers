"""Read-only online check of version-pinned arXiv metadata; no catalogue edits."""
import hashlib
import json
import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

from render import load

NS = {"a": "http://www.w3.org/2005/Atom", "x": "http://arxiv.org/schemas/atom"}


def main():
    papers = load()["papers"]
    expected = {f"{p['arxiv_id']}v{p['version']}": p for p in papers}
    ids = list(expected)
    errors = []
    seen = set()
    for offset in range(0, len(ids), 100):
        if offset:
            time.sleep(3.1)
        params = urllib.parse.urlencode({"id_list": ",".join(ids[offset:offset + 100]), "max_results": 100})
        url = "https://export.arxiv.org/api/query?" + params
        request = urllib.request.Request(url, headers={"User-Agent": "awesome-jev-papers/1.0 (source verification)"})
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                raw = response.read()
        except Exception as exc:
            raise SystemExit(f"Source verification incomplete: {type(exc).__name__}: {exc}")
        for entry in ET.fromstring(raw).findall("a:entry", NS):
            identifier = entry.findtext("a:id", "", NS).rsplit("/", 1)[-1]
            if identifier not in expected:
                errors.append("Unexpected source identifier: " + identifier)
                continue
            seen.add(identifier)
            p = expected[identifier]
            fields = {
                "title": " ".join(entry.findtext("a:title", "", NS).split()),
                "authors": [a.findtext("a:name", "", NS) for a in entry.findall("a:author", NS)],
                "first_submitted": entry.findtext("a:published", "", NS)[:10],
                "updated": entry.findtext("a:updated", "", NS)[:10],
            }
            for key, value in fields.items():
                if p[key] != value:
                    errors.append(f"{identifier}: {key} differs from pinned source")
            abstract = " ".join(entry.findtext("a:summary", "", NS).split())
            if hashlib.sha256(abstract.encode()).hexdigest() != p["source_abstract_sha256"]:
                errors.append(f"{identifier}: abstract fingerprint differs")
            for evidence in p["evidence"]:
                if evidence["location"] == "Abstract" and evidence["quote"] not in abstract:
                    errors.append(f"{identifier}: abstract evidence not found")
        print(f"Checked {min(offset + 100, len(ids))}/{len(ids)} version-pinned records.", flush=True)
    for identifier in expected.keys() - seen:
        errors.append("Missing source record: " + identifier)
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"PASS: {len(seen)} arXiv versions, metadata fields and abstract excerpts verified online.")


if __name__ == "__main__":
    main()
