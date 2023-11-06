def display_search_results(search_results):
    if search_results:
        print("Matching Files:")
        for result in search_results:
            print(result)
    else:
        print("No matching files found.")
