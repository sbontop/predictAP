import json
import os

import pytest
from _pytest.fixtures import FixtureRequest

from src.index import build_index


@pytest.mark.parametrize(
    "fixture_index_file_path, fixture_base_data_dir, fixture_expected_index, scenario",
    [
        ("existing_index_file_path", "base_data_dir", "expected_index", "load_index"),
        (
            "non_existing_index_file_path",
            "base_data_dir",
            "expected_index",
            "create_index",
        ),
    ],
)
def test_build_index(
    fixture_index_file_path: str,
    fixture_base_data_dir: str,
    fixture_expected_index: str,
    scenario: str,
    request: FixtureRequest,
):
    index_file_path = request.getfixturevalue(fixture_index_file_path)
    base_data_dir = request.getfixturevalue(fixture_base_data_dir)
    expected_index = request.getfixturevalue(fixture_expected_index)
    index = build_index(index_file_path, base_data_dir)

    assert index == expected_index

    # Remove generated files that should not exist after the test passes
    if scenario == "create_index":
        os.remove(index_file_path)
