# aggregation -> represents the realtionshiup between one object / class to another. 
#                a library can exist without its books and a book can exist without library.  

# difference between aggregation and composition and aggreagtion classes can live on its own while comp can not.

#! Aggregation "has-a" relationship -> you pass object as a parameter. so the passing of said object is in the output, not the logic code 

#___________________________________________________________________________________

class Library():
    def __init__(self, name):
        self.name = name 
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
        
    def print_books(self):
        for book in self.books:
            print(f"book {book.title} was created by {book.author}")

class Book():
    def __init__(self, title, author):
        self.title = title 
        self.author = author


# our library can exist without books
library = Library("NewYork Library")

# books can exist without library 
book1 = Book("Harry Potter", "J.K Rowling")
book2 = Book("StarWars", "George Lucas")
book3 = Book("Notes", "Mateo")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library.print_books())

#___________________________________________________________________________________
