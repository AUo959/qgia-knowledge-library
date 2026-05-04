from __future__ import annotations

import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import knowledge_contract  # noqa: E402


class KnowledgeContractTests(unittest.TestCase):
    def test_domain_derived_from_directory_name(self) -> None:
        self.assertEqual(
            knowledge_contract.domain_from_dir_name("08-crisis-protocols"),
            "crisis-protocols",
        )
        self.assertEqual(
            knowledge_contract.domain_from_dir_name("11-technology-systems"),
            "technology-systems",
        )

    def test_extract_metadata_skips_document_control_headers(self) -> None:
        sample = REPO_ROOT / "01-theoretical-foundations" / "01-01-core-ir-theories.md"
        meta = knowledge_contract.extract_metadata(sample)
        self.assertFalse(meta["summary"].startswith("**Document ID**"))
        self.assertIn("foundational international relations theories", meta["summary"].lower())

    def test_build_index_uses_directory_slug_for_domain(self) -> None:
        index = knowledge_contract.build_index(
            root=REPO_ROOT,
            generated_at="2026-04-18T00:00:00+00:00",
        )
        documents = {document["path"]: document for document in index["documents"]}
        self.assertEqual(
            documents["08-crisis-protocols/08-crisis-escalation-ladder.md"]["domain"],
            "crisis-protocols",
        )
        self.assertEqual(
            documents["09-validation-metrics/09-confidence-calibration.md"]["domain"],
            "validation-metrics",
        )
        self.assertEqual(
            documents["11-technology-systems/11-osiqp-architecture.md"]["domain"],
            "technology-systems",
        )

    def test_build_index_includes_regions_package(self) -> None:
        index = knowledge_contract.build_index(
            root=REPO_ROOT,
            generated_at="2026-04-18T00:00:00+00:00",
        )
        documents = {document["path"]: document for document in index["documents"]}
        readme = documents["regions/middle-east/iran/iran-war-2026/README.md"]
        ledger = documents["regions/middle-east/iran/iran-war-2026/baseline-ledger.md"]
        actor_cards = documents["regions/middle-east/iran/iran-war-2026/actor-cards.md"]
        scenario_catalog = documents["regions/middle-east/iran/iran-war-2026/scenario-catalog.md"]
        self.assertEqual(readme["domain"], "theater_readme")
        self.assertEqual(ledger["domain"], "ledger")
        self.assertEqual(actor_cards["domain"], "actor_cards")
        self.assertEqual(scenario_catalog["domain"], "scenario_catalog")
        self.assertEqual(
            readme["id"],
            "qgia-library:regions-middle-east-iran-iran-war-2026-readme",
        )

    def test_bootstrap_evidence_ledger_allows_empty_history(self) -> None:
        failures = knowledge_contract.validate_evidence_ledger(REPO_ROOT)
        self.assertEqual(failures, [])

    def test_bootstrap_outcome_ledger_allows_empty_history(self) -> None:
        failures = knowledge_contract.validate_outcome_ledger(REPO_ROOT)
        self.assertEqual(failures, [])

    def test_validate_repo_contract_passes(self) -> None:
        failures = knowledge_contract.validate_repo_contract(REPO_ROOT)
        self.assertEqual(failures, [])


if __name__ == "__main__":
    unittest.main()
