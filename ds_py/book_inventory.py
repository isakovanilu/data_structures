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
        
        
        