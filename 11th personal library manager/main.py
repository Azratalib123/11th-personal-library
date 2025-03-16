import json


class BookCollection:
    """A class to manage a collection of books, allowing users to store and organize their reading materials."""

    def __init__(self):
        """Initialize a new book collection with an empty list and set up file storage."""
        self.book_list = []
        self.storage_file = "books_data.json"
        self.read_from_file()

    def read_from_file(self):
        """Load saved books from a JSON file into memory. Handle errors gracefully."""
        try:
            with open(self.storage_file, "r") as file:
                self.book_list = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.book_list = []

    def save_to_file(self):
        """Store the current book collection to a JSON file."""
        with open(self.storage_file, "w") as file:
            json.dump(self.book_list, file, indent=4)

    def create_new_book(self):
        """Add a new book to the collection with user input."""
        book_title = input("Enter book title: ").strip()
        book_author = input("Enter author: ").strip()
        publication_year = input("Enter publication year: ").strip()
        book_genre = input("Enter genre: ").strip()
        is_book_read = input("Have you read this book? (yes/no): ").strip().lower() == "yes"

        new_book = {
            "title": book_title,
            "author": book_author,
            "year": publication_year,
            "genre": book_genre,
            "read": is_book_read,
        }

        self.book_list.append(new_book)
        self.save_to_file()
        print("✅ Book added successfully!\n")

    def delete_book(self):
        """Remove a book from the collection using its title."""
        book_title = input("Enter the title of the book to remove: ").strip()
        
        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                self.book_list.remove(book)
                self.save_to_file()
                print("✅ Book removed successfully!\n")
                return
        print("❌ Book not found!\n")

    def find_book(self):
        """Search for books by title or author."""
        search_text = input("Enter book title or author name to search: ").strip().lower()
        found_books = [
            book for book in self.book_list
            if search_text in book["title"].lower() or search_text in book["author"].lower()
        ]

        if found_books:
            print("📚 Matching Books:")
            for index, book in enumerate(found_books, 1):
                reading_status = "Read" if book["read"] else "Unread"
                print(f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}")
        else:
            print("❌ No matching books found.\n")

    def update_book(self):
        """Modify details of an existing book."""
        book_title = input("Enter the title of the book you want to edit: ").strip()
        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                print("Leave blank to keep existing value.")
                book["title"] = input(f"New title ({book['title']}): ").strip() or book["title"]
                book["author"] = input(f"New author ({book['author']}): ").strip() or book["author"]
                book["year"] = input(f"New year ({book['year']}): ").strip() or book["year"]
                book["genre"] = input(f"New genre ({book['genre']}): ").strip() or book["genre"]
                book["read"] = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
                self.save_to_file()
                print("✅ Book updated successfully!\n")
                return
        print("❌ Book not found!\n")

    def show_all_books(self):
        """Display all books in the collection."""
        if not self.book_list:
            print("📭 Your collection is empty.\n")
            return

        print("📚 Your Book Collection:")
        for index, book in enumerate(self.book_list, 1):
            reading_status = "Read" if book["read"] else "Unread"
            print(f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}")
        print()

    def show_reading_progress(self):
        """Display statistics about reading progress."""
        total_books = len(self.book_list)
        completed_books = sum(1 for book in self.book_list if book["read"])
        completion_rate = (completed_books / total_books * 100) if total_books > 0 else 0
        print(f"📊 Total books: {total_books}")
        print(f"📖 Reading progress: {completion_rate:.2f}%\n")

    def start_application(self):
        """Run the main application loop with a user-friendly menu."""
        while True:
            print("\n📚 Welcome to Your Book Collection Manager! 📚")
            print("1. Add a new book")
            print("2. Remove a book")
            print("3. Search for books")
            print("4. Update book details")
            print("5. View all books")
            print("6. View reading progress")
            print("7. Exit")
            user_choice = input("Please choose an option (1-7): ").strip()

            options = {
                "1": self.create_new_book,
                "2": self.delete_book,
                "3": self.find_book,
                "4": self.update_book,
                "5": self.show_all_books,
                "6": self.show_reading_progress,
            }

            if user_choice in options:
                options[user_choice]()
            elif user_choice == "7":
                self.save_to_file()
                print("👋 Thank you for using Book Collection Manager. Goodbye!")
                break
            else:
                print("❌ Invalid choice. Please try again.\n")


if __name__ == "__main__":
    book_manager = BookCollection()
    book_manager.start_application()
