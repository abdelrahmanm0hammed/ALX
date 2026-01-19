from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    class Meta:
        permissions = [
            ("can_view", "can view book"),
            ("can_create", "can create book"),
            ("can_edit", "can edit book"),
            ("can_delete","can delete book")
        ]
    def __str__(self):
        return f"{self.title} by {self.author} in {self.publication_year}"