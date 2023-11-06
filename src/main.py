"""
Driver Code
"""
from .display import display_search_results
from .index import build_index
from .input import get_search_criteria
from .search import search_files

BASE_DATA_DIR = "src/test_data"
INDEX_FILE_PATH = "src/index/index.json"


index = build_index(INDEX_FILE_PATH, BASE_DATA_DIR)
print(f"{index =}")

search_name, search_size, search_content_type = get_search_criteria()
search_results = search_files(
    index, name=search_name, size=search_size, content_type=search_content_type
)
display_search_results(search_results)
