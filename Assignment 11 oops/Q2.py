
# Book Library
# Create a class Book with fields: title, author, and price.
# Use setters to assign values and a method to print book details.

class Book_Library:
    def __init__(self,Title=None,Author=None,Price=None):
        self.__title = Title
        self.__author = Author
        self.__price = Price

    def set_book_details(self):
        title = (input("Enter Book Title : "))
        self.__title = title

        author = (input("Enter Book Author Name : "))
        self.__author = author

        price = int(input("Enter Book Price : "))
        self.__price = price

    def get_book_details(self):
        print("Book Details")
        print(f" title : {self.__title}")
        print(f" author name : {self.__author}")
        print(f" price : {self.__price}")


Book = Book_Library()
Book.set_book_details()
Book.get_book_details()