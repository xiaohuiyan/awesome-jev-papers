# Contributing

Contributions that improve coverage, translations, source accuracy and classification are welcome.

1. Check [the scope and rubric](docs/METHODOLOGY.md) and the [screening ledger](data/screening.json) before adding a paper. Prefer original arXiv records and author-linked artifacts.
2. Edit `data/papers.json`, not the generated README files. Use one version-independent arXiv ID per paper and preserve full author names. Record the version reviewed, first-submission date, revision date and verification date.
3. Choose one primary category and a relation level. Support the relationship and contribution with short exact excerpts from the abstract or a specific full-text passage. Each excerpt must be at most 80 characters and all excerpts from the paper must total at most 25 words.
4. Write concise English and Chinese summaries. Describe what was studied without turning conditional findings into general claims. A new “Jev-like” model is not automatically a reproduction of hosted Jev.
5. Add code only when the authors link it and it is publicly reachable. Record the source location and check date. Missing or inaccessible code should remain unverified.
6. Update the screening ledger, search log, statistics and changelog for new searches. Keep unresolved cases in the pending list; do not silently discard them.
7. Regenerate and check the catalogue with Python 3.10 or newer (standard library only):

```sh
python scripts/render.py
python scripts/validate.py
python -m unittest discover -s tests -v
```

For an optional read-only check against the pinned arXiv records:

```sh
python scripts/verify_sources.py
```

Source verification uses the public arXiv API and waits between requests. A network failure is an incomplete check, not proof that a paper does not exist. Routine CI is offline and does not depend on external availability.

Open a pull request describing added or changed papers and the evidence behind changed classifications. Do not upload paper PDFs, complete abstracts, API credentials or local caches. Original prose and annotations are contributed under CC BY 4.0; scripts and tests under MIT. Third-party source material retains its original rights.

## 中文

欢迎补充论文、修正翻译与分类。先查收录规则与台账，编辑结构化数据，再生成中英文目录。请提供版本明确的原始来源及短证据引文，不凭模型名称判断与 Jev 的关系。不确定的候选放入待核实清单。代码链接需由作者给出且可公开访问；未展示链接只代表尚未核实。

新增检索后同步更新统计、筛选台账和日志。提交前运行以上校验命令；不要上传论文全文、完整摘要或凭据。
