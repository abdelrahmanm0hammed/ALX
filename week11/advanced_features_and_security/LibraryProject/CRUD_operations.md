# Create Book

from bookshelf.models import Book

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book 
# Expected output< Book: 1984>


# Retrieve Book

from bookshelf.models import Book 
book = Book.objects.get(tiltle="1984")
book.id,book.title,book.author,book.publication_year
# Expected output : (1, 1984, George Orwell, 1949)

# Update Book

from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Ninteen Eighty-Four"
book.save()
book.title()
# Output: Ninteen Eighty-Four

# Delete Book
from bookshelf.models import Book 
book = Book.objects.get(title="1984")
book.delete()
book.objects.all()
# Expected output : Queryset []