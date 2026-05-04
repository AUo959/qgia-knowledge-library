#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCE_REPO = "qgia-knowledge-library"
NODE_DESIGNATION = "QGIA-CORPUS"
NODE_ROLE = "spoke"
DOWNSTREAM_NODE = "s.tag::qgia.spine"
LIVE_RUNTIME_URL = "https://www.perplexity.ai/spaces/foreign-policy-and-global-poli-_IZgsdmvSo2Yxe7LAZ5HSQ"
EXPECTED_PUBLISHED_CONTRACTS = (
    "knowledge-index",
    "evidence-record",
    "outcome-record",
)
EXPECTED_CONSUMED_CONTRACTS = (
    "constellation-event",
    "constellation-health",
    "forecast-ledger",
    "prior-table",
    "calibration-report",
    "resolution-policy",
)
INDEX_VERSION = "1.0.0"
CONTENT_DIR_PATTERN = re.compile(r"^\d{2}-.+")
SKIP_DIR_NAMES = {"references", "policies", "tests"}
SKIP_FILENAMES = {"README.md"}
SUMMARY_METADATA_LINE = re.compile(r"^\*\*[^*]+\*\*:")
EXPECTED_CONTRACT_FILES = (
    ".aurora/constellation.json",
    ".aurora/closed-loop-bootstrap.json",
    ".aurora/knowledge-index.json",
    "README.md",
    "data/intake/evidence-ledger.jsonl",
    "data/truth/outcome-ledger.jsonl",
    "references/missing-documents.md",
    "scripts/generate-knowledge-index.py",
    "scripts/validate-knowledge-contract.py",
)


def iter_content_directories(root: Path = REPO_ROOT) -> Iterable[Path]:
    for entry in sorted(root.iterdir(), key=lambda item: item.name):
        if not entry.is_dir():
            continue
        if entry.name.startswith("."):
            continue
        if entry.name in SKIP_DIR_NAMES:
            continue
        if CONTENT_DIR_PATTERN.match(entry.name):
            yield entry


def iter_markdown_documents(root: Path = REPO_ROOT) -> Iterable[Path]:
    for directory in iter_content_directories(root):
        for md_file in sorted(directory.rglob("*.md")):
            if md_file.name in SKIP_FILENAMES:
                continue
            yield md_file


def domain_from_dir_name(directory_name: str) -> str:
    if not CONTENT_DIR_PATTERN.match(directory_name):
        raise ValueError("Expected numbered content directory, got %r" % (directory_name,))
    return directory_name.split("-", 1)[1]


def git_last_modified(root: Path, relative_path: Path) -> str:
    result = subprocess.run(
        ["git", "log", "-1", "--format=%cI", "--", relative_path.as_posix()],
        cwd=root,
        text=True,
        capture_output=True,
        check=False,
    )
    timestamp = result.stdout.strip()
    if timestamp:
        return timestamp
    absolute_path = root / relative_path
    return datetime.fromtimestamp(absolute_path.stat().st_mtime, tz=timezone.utc).isoformat()


def extract_metadata(filepath: Path) -> Dict[str, Any]:
    text = filepath.read_text(encoding="utf-8")

    title_match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else filepath.stem

    checksum = hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]
    word_count = len(text.split())
    tags = [heading.strip() for heading in re.findall(r"^##\s+(.+)$", text, re.MULTILINE)]

    summary = ""
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("#"):
            continue
        if stripped.startswith("[![") or stripped.startswith("---"):
            continue
        if SUMMARY_METADATA_LINE.match(stripped):
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


def build_index(root: Path = REPO_ROOT, generated_at: Optional[str] = None) -> Dict[str, Any]:
    documents: List[Dict[str, Any]] = []

    for md_file in iter_markdown_documents(root):
        relative_path = md_file.relative_to(root)
        domain = domain_from_dir_name(relative_path.parts[0])
        meta = extract_metadata(md_file)

        documents.append(
            {
                "id": "qgia-library:%s" % md_file.stem,
                "title": meta["title"],
                "domain": domain,
                "path": relative_path.as_posix(),
                "checksum": meta["checksum"],
                "word_count": meta["word_count"],
                "last_modified": git_last_modified(root, relative_path),
                "tags": meta["tags"],
                "summary": meta["summary"],
            }
        )

    return {
        "version": INDEX_VERSION,
        "source_repo": SOURCE_REPO,
        "generated_at": generated_at or datetime.now(timezone.utc).isoformat(),
        "documents": documents,
    }


def write_index(index: Dict[str, Any], root: Path = REPO_ROOT) -> Path:
    out_path = root / ".aurora" / "knowledge-index.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(index, indent=2) + "\n", encoding="utf-8")
    return out_path


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_jsonl(path: Path) -> List[Dict[str, Any]]:
    records: List[Dict[str, Any]] = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        stripped = line.strip()
        if not stripped:
            continue
        payload = json.loads(stripped)
        if not isinstance(payload, dict):
            raise ValueError("%s line %s must decode to a JSON object" % (path, line_no))
        records.append(payload)
    return records


def is_iso_datetime(value: Any) -> bool:
    if not isinstance(value, str) or not value:
        return False
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return False
    return True


def validate_evidence_ledger(root: Path) -> List[str]:
    failures: List[str] = []
    path = root / "data/intake/evidence-ledger.jsonl"
    try:
        records = parse_jsonl(path)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        return ["evidence ledger invalid: %s" % exc]

    for index, record in enumerate(records):
        prefix = "evidence ledger record %s" % index
        if record.get("record_type") != "evidence":
            failures.append("%s must have record_type=evidence" % prefix)
        if not isinstance(record.get("evidence_id"), str):
            failures.append("%s missing evidence_id" % prefix)
        if not is_iso_datetime(record.get("observed_at")):
            failures.append("%s has invalid observed_at" % prefix)
        if not is_iso_datetime(record.get("ingested_at")):
            failures.append("%s has invalid ingested_at" % prefix)
        topic_refs = record.get("topic_refs")
        if not isinstance(topic_refs, list) or not topic_refs:
            failures.append("%s must declare non-empty topic_refs" % prefix)
    return failures


def validate_outcome_ledger(root: Path) -> List[str]:
    failures: List[str] = []
    path = root / "data/truth/outcome-ledger.jsonl"
    try:
        records = parse_jsonl(path)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        return ["outcome ledger invalid: %s" % exc]

    for index, record in enumerate(records):
        prefix = "outcome ledger record %s" % index
        if record.get("record_type") != "outcome":
            failures.append("%s must have record_type=outcome" % prefix)
        if not isinstance(record.get("outcome_id"), str):
            failures.append("%s missing outcome_id" % prefix)
        if not isinstance(record.get("forecast_id"), str):
            failures.append("%s missing forecast_id" % prefix)
        if not is_iso_datetime(record.get("resolved_at")):
            failures.append("%s has invalid resolved_at" % prefix)
        adjudication = record.get("adjudication")
        if not isinstance(adjudication, dict):
            failures.append("%s missing adjudication" % prefix)
            continue
        evidence_refs = adjudication.get("evidence_refs")
        if not isinstance(evidence_refs, list) or not evidence_refs:
            failures.append("%s must declare non-empty adjudication.evidence_refs" % prefix)
    return failures


def validate_repo_contract(root: Path = REPO_ROOT) -> List[str]:
    failures: List[str] = []

    for relative in EXPECTED_CONTRACT_FILES:
        if not (root / relative).exists():
            failures.append("Missing required contract file: %s" % relative)

    if failures:
        return failures

    constellation = load_json(root / ".aurora" / "constellation.json")
    node = constellation.get("node", {})
    contracts = constellation.get("contracts", {})
    downstream = constellation.get("downstream", [])
    health = constellation.get("health", {})
    meta = constellation.get("meta", {})

    if node.get("designation") != NODE_DESIGNATION:
        failures.append(
            "constellation designation mismatch: expected %s, got %r"
            % (NODE_DESIGNATION, node.get("designation"))
        )
    if node.get("repo") != SOURCE_REPO:
        failures.append(
            "constellation repo mismatch: expected %s, got %r"
            % (SOURCE_REPO, node.get("repo"))
        )
    if node.get("role") != NODE_ROLE:
        failures.append(
            "constellation role mismatch: expected %s, got %r"
            % (NODE_ROLE, node.get("role"))
        )
    published = contracts.get("published", [])
    consumed = contracts.get("consumed", [])
    for contract_name in EXPECTED_PUBLISHED_CONTRACTS:
        if contract_name not in published:
            failures.append("constellation contracts must publish %s" % contract_name)
    for contract_name in EXPECTED_CONSUMED_CONTRACTS:
        if contract_name not in consumed:
            failures.append("constellation contracts must consume %s" % contract_name)
    if DOWNSTREAM_NODE not in downstream:
        failures.append("constellation downstream must include %s" % DOWNSTREAM_NODE)
    if health.get("closed_loop_stage") != "library-bootstrap":
        failures.append("constellation health.closed_loop_stage must be library-bootstrap")
    if meta.get("contract_package_ref") != "qgia_knowledge_closed_loop_contract_v1":
        failures.append("constellation meta.contract_package_ref must be qgia_knowledge_closed_loop_contract_v1")
    runtime_targets = meta.get("runtime_targets")
    if not isinstance(runtime_targets, list) or not runtime_targets:
        failures.append("constellation meta.runtime_targets must declare at least one runtime target")
    else:
        matched_runtime = False
        for target in runtime_targets:
            if not isinstance(target, dict):
                continue
            if (
                target.get("platform") == "perplexity"
                and target.get("designation") == "declared-live-runtime"
                and target.get("verification") == "user-declared"
                and target.get("url") == LIVE_RUNTIME_URL
            ):
                matched_runtime = True
                break
        if not matched_runtime:
            failures.append("constellation meta.runtime_targets must include the declared Perplexity live runtime")

    bootstrap = load_json(root / ".aurora" / "closed-loop-bootstrap.json")
    if bootstrap.get("artifact") != "qgia_library_closed_loop_bootstrap":
        failures.append("closed-loop bootstrap receipt has unexpected artifact id")
    if bootstrap.get("stage") != "library-bootstrap":
        failures.append("closed-loop bootstrap receipt must declare stage library-bootstrap")
    if bootstrap.get("contract_package_ref") != "qgia_knowledge_closed_loop_contract_v1":
        failures.append("closed-loop bootstrap receipt must reference qgia_knowledge_closed_loop_contract_v1")

    index = load_json(root / ".aurora" / "knowledge-index.json")
    if index.get("version") != INDEX_VERSION:
        failures.append(
            "knowledge index version mismatch: expected %s, got %r"
            % (INDEX_VERSION, index.get("version"))
        )
    if index.get("source_repo") != SOURCE_REPO:
        failures.append(
            "knowledge index source_repo mismatch: expected %s, got %r"
            % (SOURCE_REPO, index.get("source_repo"))
        )

    expected_index = build_index(root=root, generated_at=index.get("generated_at"))
    if index.get("documents") != expected_index.get("documents"):
        failures.append(
            "knowledge index is stale or inconsistent with repository content; rerun scripts/generate-knowledge-index.py"
        )

    for document in index.get("documents", []):
        summary = str(document.get("summary", "")).strip()
        path = str(document.get("path", ""))
        if summary.startswith("**Document ID**"):
            failures.append("knowledge index summary still contains document-control metadata for %s" % path)
        if not summary:
            failures.append("knowledge index summary is empty for %s" % path)

    failures.extend(validate_evidence_ledger(root))
    failures.extend(validate_outcome_ledger(root))

    return failures


def main_generate() -> int:
    index = build_index()
    out_path = write_index(index)
    print("Generated knowledge index: %s documents -> %s" % (len(index["documents"]), out_path))
    return 0


def main_validate() -> int:
    failures = validate_repo_contract()
    if failures:
        print("Knowledge contract validation failed:")
        for failure in failures:
            print("- %s" % failure)
        return 1
    print("Knowledge contract validation passed.")
    return 0
