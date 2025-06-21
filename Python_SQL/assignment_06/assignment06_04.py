#  Design a system where a Library manages multiple Books, and each Book has an ID, title,
# and author.
# Functionalities:
# Add a Book to the library.
# Display all Books in the library.
# Exit the system when done.
from random import choice


class Book:
    def __init__(self,book_id, book_name, author):
        self.book_id = book_id
        self.book_name = book_name
        self.author = author

    def __str__(self):
        return (f"ID : {self.book_id}, Book name : {self.book_name}, Author : {self.author}")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        book_id = input("Enter the id : ")
        book_name = input("Enter the book name : ")
        author = input("Enter the Author name : ")
        book = Book(book_id, book_name, author)
        self.books.append(book)
        print("Book added Successfully \n ")

    def display_books(self):
        if not self.books:
            print(f" No Book in library ")
        else:
            print("Book in Library")
            for book in self.books:
                print(book)
            print()

    def run(self):
        while True:
            print("Library Management System ...")
            print("1. Add book ")
            print("2. Display book ")
            print("3. exit from library ")
            choice = input("Enter your choice : ")

            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.display_books()
            elif choice == "3":
                print("Exit")
                break
            else:
                print(f"Invalid choice")


if __name__ == "__main__":
    library = Library()
    library.run()