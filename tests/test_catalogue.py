"""Regression checks for errors that would corrupt a public reading list."""
import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from render import load
from validate import validate


class CatalogueValidation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = load()

    def altered(self):
        return copy.deepcopy(self.data)

    def test_duplicate_arxiv_id_rejected(self):
        data = self.altered()
        data["papers"].append(copy.deepcopy(data["papers"][0]))
        self.assertIn("Duplicate arXiv IDs", validate(data))

    def test_wrong_version_link_rejected(self):
        data = self.altered()
        data["papers"][0]["reviewed_url"] += "0"
        self.assertTrue(any("wrong reviewed URL" in s for s in validate(data)))

    def test_missing_evidence_rejected(self):
        data = self.altered()
        data["papers"][0]["evidence"] = []
        self.assertTrue(any("missing criterion evidence" in s for s in validate(data)))

    def test_future_version_rejected(self):
        data = self.altered()
        data["papers"][0]["updated"] = "2099-01-01"
        self.assertTrue(any("inconsistent dates" in s for s in validate(data)))

    def test_missing_translation_rejected(self):
        data = self.altered()
        data["papers"][0]["summary"]["zh"] = ""
        self.assertTrue(any("missing zh annotation" in s for s in validate(data)))


if __name__ == "__main__":
    unittest.main()
