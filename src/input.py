"""
Input Data from user
"""


def get_search_criteria() -> tuple[str, str, str]:
    """
    Get search criteria
    :return:
    """
    search_name = input("Enter file name (or press Enter to skip): ").strip() or ""
    search_size = input("Enter file size (or press Enter to skip): ").strip() or ""
    search_size = str(int(search_size)) if search_size and search_size.isdigit() else ""
    search_content_type = (
        input("Enter content type (or press Enter to skip): ").strip() or ""
    )
    return search_name, search_size, search_content_type
