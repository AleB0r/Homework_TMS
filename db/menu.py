import sys

from repository import Repository


class Menu:
    def __init__(self, repository: Repository) -> None:
        self.items = [
            "Show Books",
            "Add Book",
            "Update Book",
            "Delete Book",
            "Show Authors",
            "Add Author",
            "Find Book",
            "Exit",
        ]
        self.methods = [
            self.show_all_books,
            self.add_book,
            self.update_book,
            self.delete_book,
            self.show_authors,
            self.add_author,
            self.find_book,
            self.exit_menu
        ]
        self.repository = repository

    def show_menu(self):
        print(*enumerate(self.items, start=1), sep='\n')
        item = input("Choice item: ")
        method = self.pick_item(item)
        return method()

    def pick_item(self, item):
        try:
            item = int(item)
            if 1 <= item <= len(self.items):
                return self.methods[item - 1]
            else:
                print("Invalid choice. Please select a valid item.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def exit_menu(self):
        sys.exit()

    def show_all_books(self):
        books = self.repository.show_all_books()
        return print(*books, sep='\n')

    def add_book(self):
        book_name = input("Enter book name: ")
        authors = self.repository.show_authors()
        author_count = len(authors)
        print("Authors:")
        for author in authors:
            print(author)
        check = False
        while not check:
            try:
                author_id = int(input(f"Choice author number (1-{author_count}): "))
                if author_id < 1 or author_id > author_count:
                    print("Invalid author number. Please try again.")
                else:
                    check = True
            except ValueError:
                print("Invalid input. Please enter a number.")

        return self.repository.add_book(book_name, author_id)

    def update_book(self):
        books = self.repository.show_all_books()
        books_count = len(books)
        print("Books:")
        for book in books:
            print(book)
        check = False
        while not check:
            try:
                book_id = int(input(f"Choice book number (1-{books_count}): "))
                if book_id < 1 or book_id > books_count:
                    print("Invalid book number. Please try again.")
                else:
                    check = True
            except ValueError:
                print("Invalid input. Please enter a number.")
        new_book_name = input("Enter new book name: ")
        return self.repository.update_book(book_id, new_book_name)

    def delete_book(self):
        books = self.repository.show_all_books()
        books_count = len(books)
        print("Books:")
        for book in books:
            print(book)
        check = False
        while not check:
            try:
                book_id = int(input(f"Choice book number (1-{books_count}): "))
                if book_id < 1 or book_id > books_count:
                    print("Invalid book number. Please try again.")
                else:
                    check = True
            except ValueError:
                print("Invalid input. Please enter a number.")
        return self.repository.delete_book(book_id)

    def show_authors(self):
        authors = self.repository.show_authors()
        return print(*authors, sep='\n')

    def add_author(self):
        author_name = input("Enter author name: ")
        return self.repository.add_author(author_name)

    def find_book(self):
        book_name = input("Enter book name: ")
        books = self.repository.find_book(book_name)
        if books:
            print("Found books:")
            for book in books:
                print(book)
        else:
            print("No books found.")
