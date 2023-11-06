"""
Search module
"""

from typing import Any


def search_files(
    index: dict[str, Any], name: str = "", size: str = "", content_type: str = ""
) -> list[str]:
    """
    Perform search by multiple different arguments
    :param index:
    :param name:
    :param size:
    :param content_type:
    :return:
    """
    results = []
    print(f"{name =}, {size = }, {content_type = }")
    if (not name) and (not size) and (not content_type):
        return []

    for file_name, file_info in index.items():
        matches_name = (not name) or (name.lower() in file_name.lower())
        matches_size = (not size) or (str(file_info["size"]) == str(size))
        matches_content_type = (not content_type) or (
            content_type.lower() in file_info["content_type"].lower()
        )

        if matches_name and matches_size and matches_content_type:
            results.append(file_name)

    return results
