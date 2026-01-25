from django.db import models

class Author(models.Model):
    
    """
    Author model
    
    this model is used to store data for the author and it include field name (CharField) to store 
    the name of the author
    
    """
    name = models.CharField(max_length=100) # name is a (CharField) of maximum length of 100 characters to store the author's name



class Book(models.Model):
    """
    Book model

    This model represents a book in the library system.
    It stores book information including title, publication_year, and maintains a foreign key relationship
    to the Author model to associate each book with its author
    
    Attributes:
    title(CharField):the title of the book, max length 200 characters
    publication_year (integerField): The year the book was published
    author(ForeignKey): Reference to the author model. CASCADE delete ensures that if an author is deleted,
    all their books are also deleted. related_name= 'books' allows reverse

    """
    title = models.CharField(max_length=200)  # title is a CharField storing the book's title, max 200 characters
    publication_year = models.IntegerField()  # publication_year is an IntegerField storing the year of publication
    author = models.ForeignKey(Author,on_delete=models.CASCADE, related_name= "books")  # ForeignKey to Author model with CASCADE delete and reverse relation


