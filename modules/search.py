def search_by_title(keyword):
    """
    Searches for a book by title or author (case insensitive).
    """
    found = False
    keyword = keyword.lower() # Make search case-insensitive
    
    try:
        with open("books.txt", "r") as f:
            print(f"\n--- Search Results for '{keyword}' ---")
            print(f"{'ID':<5} {'Title':<20} {'Status':<10}")
            print("-" * 35)
            
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 4:
                    # Check if keyword is in Title or Author
                    if keyword in parts[1].lower() or keyword in parts[2].lower():
                        print(f"{parts[0]:<5} {parts[1]:<20} {parts[3]:<10}")
                        found = True
            
            if not found:
                print("No books found matching that keyword.")
                
    except FileNotFoundError:
        print("Error: Database not found.")