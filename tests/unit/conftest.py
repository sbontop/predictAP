from typing import Any

import pytest


@pytest.fixture(name="existing_index_file_path")
def existing_index_file_path() -> str:
    return "tests/data/test_index_does_exist.json"


@pytest.fixture(name="non_existing_index_file_path")
def non_existing_index_file_path() -> str:
    return "tests/data/test_index_does_not_exist.json"


@pytest.fixture(name="base_data_dir")
def base_data_dir() -> str:
    return "tests/data/samuel_test_data"


@pytest.fixture(name="expected_index")
def expected_index() -> dict[str, Any]:
    return {
        "dummy_image_2.jpg": {"size": 823, "content_type": "image/jpeg"},
        "dummy_image_1.jpg": {"size": 823, "content_type": "image/jpeg"},
        "dummy_image_0.jpg": {"size": 823, "content_type": "image/jpeg"},
        "user1.json": {"size": 39, "content_type": "application/json"},
        "user2.json": {"size": 39, "content_type": "application/json"},
    }
