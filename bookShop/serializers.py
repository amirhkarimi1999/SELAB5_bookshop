from rest_framework import serializers
from .models import Book, BOOK_CATEGORIES_CHOICES, OTHER

# Book Serializer
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'category', 'price']