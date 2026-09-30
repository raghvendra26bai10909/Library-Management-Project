def load_books():
    """Reads books from file into a list of dictionaries."""
    books = []
    try:
        with open("books.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 4:
                    books.append({
                        "id": parts[0], "title": parts[1],
                        "author": parts[2], "status": parts[3]
                    })
    except FileNotFoundError:
        open("books.txt", "w").close() # Create if missing
    return books

def view_books():
    """Displays all books in a formatted way."""
    books = load_books()
    print("\n--- Library Inventory ---")
    print(f"{'ID':<5} {'Title':<20} {'Status':<10}")
    print("-" * 35)
    for book in books:
        print(f"{book['id']:<5} {book['title']:<20} {book['status']:<10}")
    print("-" * 35)

def add_book(id, title, author):
    """Appends a new book to the file."""
    with open("books.txt", "a") as f:
        f.write(f"\n{id},{title},{author},Available")
    print("Book added successfully!")