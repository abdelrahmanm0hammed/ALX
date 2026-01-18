from .models import Author, Book, Library, Librarian

#Query all books by a specific author
author = Author.objects.get(name='author_name')
books = author.books.all()

#List all books in a library.
library = Library.objects.get(name='library_name')
books = library.books.all()

#Retrieve the librarian for a library.

library = Library.objects.get(name='library_name')
librarian = library.librarian