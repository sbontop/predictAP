from src.display import display_search_results
from src.index import build_index
from src.input import get_search_criteria
from src.search import search_files

BASE_DATA_DIR = "test_data"
INDEX_FILE_PATH = "index/index.json"


index = build_index(INDEX_FILE_PATH, BASE_DATA_DIR)
print(f"{index = }")

search_name, search_size, search_content_type = get_search_criteria()
search_results = search_files(
    index, name=search_name, size=search_size, content_type=search_content_type
)
display_search_results(search_results)
