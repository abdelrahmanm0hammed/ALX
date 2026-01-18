from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    publication_year = models.IntegerField(default=2025)
    class Meta:
        permissions = [
            ("can_add_book" , "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book")
        ]
            
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='libraries')

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

class UserProfile(models.Model):
    ROLE_CHOICES ={ "ADMIN":"Admin",
        "LIBRARIAN":"Librarian",
        "MEMBER":"Member"}
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(choices=ROLE_CHOICES,default='MEMBER'
    )
    def __str__(self):
        return f"{self.user.username} - {self.role}"

        
