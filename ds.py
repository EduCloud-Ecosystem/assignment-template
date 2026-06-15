"""
<HW-NN>: <Assignment Title>

<One or two sentences describing what students build in this module.>

Replace this docstring and the example functions below with your assignment.
This skeleton uses only the Python standard library, so it runs on a stock
`python` image with no setup. See the README for adding third-party packages
(pandas, scikit-learn, ...) via a grading image.
"""

import csv

# pylint: disable=invalid-name


def load_rows(file_path: str) -> list:
    """
    Read a CSV file and return its rows as a list of dicts (one dict per row).
    """
    # TODO: open file_path and use csv.DictReader to return a list of dict rows.
    raise NotImplementedError("Implement load_rows()")


def clean_rows(rows: list) -> list:
    """
    Return only the rows whose values are all non-empty.
    """
    # TODO: keep rows where every value is non-empty.
    raise NotImplementedError("Implement clean_rows()")


def add_field(rows: list, src: str, dest: str) -> list:
    """
    Return rows with a new field `dest` derived from the numeric field `src`
    (for example, `src` doubled). Leave the other fields unchanged.
    """
    # TODO: for each row, set row[dest] from float(row[src]); return the rows.
    raise NotImplementedError("Implement add_field()")


def mean_of(rows: list, field: str) -> float:
    """
    Return the mean of the numeric `field` across all rows.
    """
    # TODO: compute and return the average of float(row[field]) over rows.
    raise NotImplementedError("Implement mean_of()")
