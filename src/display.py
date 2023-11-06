"""
Display module
"""


def display_search_results(search_results: list[str]) -> None:
    """
    Display search results
    :param search_results:
    :return:
    """
    if search_results:
        print("Matching Files:")
        for result in search_results:
            print(result)
    else:
        print("No matching files found.")
