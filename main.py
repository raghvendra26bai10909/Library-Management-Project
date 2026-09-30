from modules import book_ops, search
from modules import lending
# Import other modules as you create them

def main_menu():
    while True:
        print("\n=== VIT Library Manager ===")
        print("1. View All Books")
        print("2. Search Book by Title")
        print("3. Add New Book")
        print("4. Borrow a Book")
        print("5. Return a Book")
        print("6. Exit")
        
        choice = input("Enter choice: ")

        if choice == '1':
            book_ops.view_books()
        elif choice == '2':
            keyword = input("Enter search keyword: ")
            search.search_by_title(keyword) # You need to create this in search.py
        elif choice == '3':
            # Basic Input
            bid = input("Enter Book ID: ")
            btitle = input("Enter Title: ")
            bauth = input("Enter Author: ")
            book_ops.add_book(bid, btitle, bauth)
        elif choice == '6':
            print("Exiting...")
        elif choice == '4':
            bid = input("Enter Book ID to Borrow: ")
            lending.borrow_book(bid)
        elif choice == '5':
            bid = input("Enter Book ID to Return: ")
            lending.return_book(bid)
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main_menu()