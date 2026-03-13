#!/usr/bin/env python3
"""Generate .aurora/knowledge-index.json for the QGIA Knowledge Library.

Walks all content directories (01-* through 12-*), extracts metadata from
each Markdown file, and writes a structured index conforming to the
Aurora Constellation knowledge-index contract.
"""

import hashlib
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

DOMAIN_MAP = {
    "01": "theoretical-foundations",
    "02": "analytical-frameworks",
    "03": "regional-expertise",
    "04": "functional-domains",
    "05": "operational-methods",
    "06": "quantitative-models",
    "07": "crisis-protocols",
    "08": "validation-metrics",
    "09": "intelligence-tradecraft",
    "10": "technology-domains",
    "11": "economic-intelligence",
    "12": "emerging-threats",
}

SKIP_DIRS = {"references", "policies"}
SKIP_FILES = {"README.md"}


def extract_metadata(filepath: Path) -> dict | None:
    """Extract title, tags, summary, word count, and checksum from a Markdown file."""
    text = filepath.read_text(encoding="utf-8")

    # H1 title
    m = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    title = m.group(1).strip() if m else filepath.stem

    # SHA-256 checksum (first 16 hex chars)
    checksum = hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]

    # Word count
    word_count = len(text.split())

    # H2 headings as tags
    tags = [h.strip() for h in re.findall(r"^##\s+(.+)$", text, re.MULTILINE)]

    # First non-heading, non-empty paragraph as summary (max 300 chars)
    summary = ""
    for line in text.split("\n"):
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("#"):
            continue
        # Skip badge lines and horizontal rules
        if stripped.startswith("[![") or stripped.startswith("---"):
            continue
        summary = stripped[:300]
        break

    return {
        "title": title,
        "checksum": checksum,
        "word_count": word_count,
        "tags": tags,
        "summary": summary,
    }


def main() -> None:
    documents = []

    for entry in sorted(REPO_ROOT.iterdir()):
        if not entry.is_dir():
            continue
        if entry.name.startswith("."):
            continue
        if entry.name in SKIP_DIRS:
            continue

        prefix = entry.name[:2]
        domain = DOMAIN_MAP.get(prefix)
        if domain is None:
            continue

        for md_file in sorted(entry.rglob("*.md")):
            if md_file.name in SKIP_FILES:
                continue

            rel_path = md_file.relative_to(REPO_ROOT)
            meta = extract_metadata(md_file)
            if meta is None:
                continue

            # Last modified time from filesystem
            mtime = datetime.fromtimestamp(
                md_file.stat().st_mtime, tz=timezone.utc
            ).isoformat()

            doc_id = f"qgia-library:{md_file.stem}"

            documents.append(
                {
                    "id": doc_id,
                    "title": meta["title"],
                    "domain": domain,
                    "path": str(rel_path),
                    "checksum": meta["checksum"],
                    "word_count": meta["word_count"],
                    "last_modified": mtime,
                    "tags": meta["tags"],
                    "summary": meta["summary"],
                }
            )

    index = {
        "version": "1.0.0",
        "source_repo": "qgia-knowledge-library",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "documents": documents,
    }

    out_path = REPO_ROOT / ".aurora" / "knowledge-index.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(index, indent=2) + "\n", encoding="utf-8")

    print(f"Generated knowledge index: {len(documents)} documents → {out_path}")


if __name__ == "__main__":
    main()
