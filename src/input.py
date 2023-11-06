def get_search_criteria():
    search_name = input("Enter file name (or press Enter to skip): ").strip() or None
    search_size = input("Enter file size (or press Enter to skip): ").strip() or None
    search_size = int(search_size) if search_size.isdigit() else None
    search_content_type = (
        input("Enter content type (or press Enter to skip): ").strip() or None
    )
    return search_name, search_size, search_content_type
