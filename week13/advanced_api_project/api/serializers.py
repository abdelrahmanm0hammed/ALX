from .models import Author, Book
from rest_framework import serializers
from datetime import datetime

class AuthorSerializer(serializers.ModelSerializer):
    """
    AuthorSerializer
    
    This serializer is used to serialize and deserialize Author model instances to/from JSON format.
    It's used in API endpoints to convert Author objects to JSON responses and JSON requests back to Author objects.
    
    Exposes only the 'name' field from the Author model.
    """
    class Meta:
        model = Author
        fields = ['name']


class BookSerializer(serializers.ModelSerializer):
    """
    BookSerializer
    
    This serializer is used to serialize and deserialize Book model instances to/from JSON format.
    It's used in API endpoints to handle book data in HTTP requests and responses.
    
    Includes custom validation via validate_publication_year() method to ensure that the publication year
    is not set to a future date. This prevents invalid data from being created or updated.
    
    Exposes fields: title, publication_year, and author from the Book model.
    """
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                f"publication year cannot be in the future. current year is {current_year}"
            )
        return value
    