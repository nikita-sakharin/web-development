from rest_framework.serializers import (CharField, DateField, DecimalField,
    ModelSerializer, Serializer)

from main.models import Book, Genre

class AuthorSerializer(Serializer):
    full_name = CharField(max_length=255)
    birth_date = DateField()
    death_date = DateField()

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        exclude = ['id']

class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        exclude = ['id']
