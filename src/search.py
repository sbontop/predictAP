from typing import Any


def search_files(
    index: dict[str, Any], name: str = None, size: str = None, content_type: str = None
) -> list[str]:
    results = []

    if name is None and size is None and content_type is None:
        return []

    for file_name, file_info in index.items():
        matches_name = (name is None) or (name.lower() in file_name.lower())
        matches_size = (size is None) or (str(file_info["size"]) == str(size))
        matches_content_type = (content_type is None) or (
            content_type.lower() == file_info["content_type"].lower()
        )

        if matches_name and matches_size and matches_content_type:
            results.append(file_name)

    return results