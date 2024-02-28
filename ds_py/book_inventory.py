"""
Book Inventory System: Implement a Book class 
with attributes for title, author, and ISBN, 
and a Library class to manage a collection of
Book objects, 
including methods to add, remove, and display books.
"""

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        
    def __str__(self):
        return f"{self.title} by {self.author} ({self.isbn})"
         
class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        
    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                pass