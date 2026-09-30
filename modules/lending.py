def borrow_book(book_id):
    """Changes status from Available to Borrowed."""
    updated_lines = []
    found = False
    
    try:
        # Step 1: Read all data
        with open("books.txt", "r") as f:
            lines = f.readlines()
            
        # Step 2: Modify the specific line
        for line in lines:
            parts = line.strip().split(",")
            if len(parts) == 4 and parts[0] == book_id:
                found = True
                if parts[3] == "Available":
                    parts[3] = "Borrowed"
                    print(f"Success: You have borrowed '{parts[1]}'.")
                else:
                    print(f"Error: '{parts[1]}' is already borrowed.")
                # Reconstruct the line
                line = ",".join(parts) + "\n"
            updated_lines.append(line)
            
        # Step 3: Write everything back if found
        if found:
            with open("books.txt", "w") as f:
                f.writelines(updated_lines)
        else:
            print("Error: Book ID not found.")

    except FileNotFoundError:
        print("Error: Database not found.")

def return_book(book_id):
    """Changes status from Borrowed to Available."""
    updated_lines = []
    found = False
    
    try:
        with open("books.txt", "r") as f:
            lines = f.readlines()
            
        for line in lines:
            parts = line.strip().split(",")
            if len(parts) == 4 and parts[0] == book_id:
                found = True
                if parts[3] == "Borrowed":
                    parts[3] = "Available"
                    print(f"Success: You have returned '{parts[1]}'.")
                else:
                    print(f"Info: '{parts[1]}' was not borrowed.")
                line = ",".join(parts) + "\n"
            updated_lines.append(line)
            
        if found:
            with open("books.txt", "w") as f:
                f.writelines(updated_lines)
        else:
            print("Error: Book ID not found.")

    except FileNotFoundError:
        print("Error: Database not found.")