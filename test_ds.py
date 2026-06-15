"""Unit tests for ds.py. Students should not modify this file."""

import csv
import os
import unittest

from ds import load_rows, clean_rows, add_field, mean_of


class TestAssignment(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Small synthetic dataset so the tests don't depend on the real data file.
        cls.rows = [
            {"id": "1", "value": "10"},
            {"id": "2", "value": "20"},
            {"id": "3", "value": "30"},
            {"id": "4", "value": "40"},
        ]

    def test_load_rows(self):
        path = "temp_test.csv"
        with open(path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "value"])
            writer.writeheader()
            writer.writerows(self.rows)
        loaded = load_rows(path)
        os.remove(path)
        self.assertEqual(len(loaded), len(self.rows))
        self.assertEqual(loaded[0]["value"], "10")

    def test_clean_rows(self):
        dirty = [dict(r) for r in self.rows] + [{"id": "5", "value": ""}]
        cleaned = clean_rows(dirty)
        self.assertEqual(len(cleaned), len(self.rows))

    def test_add_field(self):
        out = add_field([dict(r) for r in self.rows], "value", "value_x2")
        self.assertIn("value_x2", out[0])

    def test_mean_of(self):
        result = mean_of([dict(r) for r in self.rows], "value")
        self.assertAlmostEqual(float(result), 25.0)


if __name__ == "__main__":
    unittest.main()
