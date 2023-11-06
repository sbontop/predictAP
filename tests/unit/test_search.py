import pytest

from src.search import search_files


@pytest.mark.parametrize(
    "name, size, content_type, expected_result",
    [
        (None, None, None, []),  # Success: No matching results
        ("NON_EXISTING_USER", None, None, []),  # Success: No matching results
        (
            "user1.json",
            None,
            None,
            ["user1.json"],
        ),  # Success: Search by name, full string match
        (
            "user",
            None,
            None,
            ["user1.json", "user2.json"],
        ),  # Success: Search by name, partial string match
        (
            "USER",
            None,
            None,
            ["user1.json", "user2.json"],
        ),  # Success: Search by name, partial string match case insensitive
        (
            "dummy_image_1.jpg",
            823,
            None,
            ["dummy_image_1.jpg"],
        ),  # Success: Search by name and size
        (
            "DUMMY_IMAGE_1.jpg",
            823,
            None,
            ["dummy_image_1.jpg"],
        ),  # Success: Search by name and size case insensitive
        (
            "dummy_image_1.jpg",
            823,
            "image/jpeg",
            ["dummy_image_1.jpg"],
        ),  # Success: Search by name, size and type
    ],
)
def test_search_files(expected_index, name, size, content_type, expected_result):
    results = search_files(expected_index, name, size, content_type)
    assert results == expected_result
