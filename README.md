 VIT Library Manager 📚

## Overview
The **VIT Library Manager** is a CLI based application created in which the user gets multiple options and features like book management, search ability, lending system, data persistence, etc. The application is made using Python language only

## Features
* **Book Management:** Add new books to the database (ID, Title, Author).
* **Search Functionality:** Find books by title or author keywords.
* **Lending System:** Borrow and return books, updating their status in real-time.
* **Data Persistence:** All data is saved automatically to `books.txt`, ensuring no data loss.
* **Input Validation:** Prevents errors (e.g., trying to borrow a book that doesn't exist).

## Technologies Used
* **Language:** Python 3.x
* **Concepts:** File Handling, Modular Programming, Exception Handling, Lists & Dictionaries.

## Instructions for Testing
1.  **Add a Book:** Select Option 3 and enter details (e.g., ID: 105, Title: "Dark Matter").
2.  **View Books:** Select Option 1 to confirm the book was added.
3.  **Borrow a Book:** Select Option 5, enter ID 105. The status should change to "Borrowed".
4.  **Search:** Select Option 2 and type "Dark". The book should appear in results.

