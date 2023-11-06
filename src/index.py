"""
Module Index
"""

import json
import mimetypes
import os
from typing import Any


def _create_index(index_file_path: str, base_data_dir: str) -> dict[str, Any]:
    print(f"Creating Index for {index_file_path = } on dir {base_data_dir = }")
    index = _traverse_directory(base_data_dir)
    with open(index_file_path, "w", encoding="utf-8") as index_file:
        json.dump(index, index_file)
    return index


def _load_index(index_file_path: str) -> Any:
    with open(index_file_path, "r", encoding="utf-8") as index_file:
        return json.load(index_file)


def _traverse_directory(directory: str) -> dict[str, Any]:
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory does not exist: {directory}")
    index = {}
    try:
        for root, _, files in os.walk(directory):
            print(f"{files = }")
            for file in files:
                file_path = os.path.join(root, file)
                file_name = os.path.basename(file_path)
                file_size = os.path.getsize(file_path)
                content_type, _ = mimetypes.guess_type(file_path)
                index[file_name] = {"size": file_size, "content_type": content_type}
    except Exception as e:  # pylint: disable=W0718
        print(f"An unexpected error occurred while traversing the directory: {str(e)}")
    return index


def build_index(index_file_path: str, base_data_dir: str) -> Any:
    """
    Build Index
    :param index_file_path:
    :param base_data_dir:
    :return:
    """
    if os.path.exists(index_file_path):
        return _load_index(index_file_path)
    return _create_index(index_file_path, base_data_dir)
