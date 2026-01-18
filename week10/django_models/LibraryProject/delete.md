# Delete Book
from bookshelf.models import Book 
book = Book.objects.get(title="1984")
book.delete()
book.objects.all()
# Expected output : Queryset []