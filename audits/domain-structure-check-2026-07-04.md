# QGIA Domain Structure Drift Check Receipt

Added guard: `scripts/knowledge_contract.py` now compares the README
`Repository Structure` tree against the live top-level QGIA domain folders and
the immediate `regions/*` corpus groups.

Run:

```bash
python3 scripts/validate-knowledge-contract.py
python3 -m unittest discover -s tests
```

Automatic coverage: `.github/workflows/constellation-knowledge-index.yml`
already runs the validator and unittest suite on pushes that touch Markdown,
data, scripts, or tests.

Protects:

- README structure entries that name folders absent from the corpus tree.
- Live numbered domain folders or `regions/*` groups missing from the README.
- Region-folder drift such as a new active theater directory without a matching
  README declaration.
