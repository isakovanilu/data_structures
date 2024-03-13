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
        if not any(b.isbn == book.isbn for b in self.books):
            self.books.append(book)
        else:
            print('Book is here')
        
    def search_books(self, keyword):
        found_books = [book for book in self.books if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower() or keyword == book.isbn]
        if found_books:
            for book in found_books:
                print('Found: ', book)
        else:
            print("No matching books found.")
            
    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                break
        else:
            print("Book not found.")
                
    def display_books(self):
        for book in self.books:
            print(book)
            
library = Library()
library.add_book(Book("Mindset", "C. Dweck", "978-0316769345"))
library.add_book(Book("Code Craftw", "P. Goodliffe", "978-00609352346"))
library.add_book(Book("Code Craft", "P. Goodliffe", "978-00609352345"))

library.display_books()
library.remove_book("978-00609352345")
library.display_books()
library.search_books('Mindset')
library.display_books()

