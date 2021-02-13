from rest_framework.serializers import (CharField, DateField, DecimalField,
    ModelSerializer, Serializer)

from main.models import Book

class AuthorSerializer(Serializer):
    full_name = CharField(max_length=255)
    birth_date = DateField()
    death_date = DateField()

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        exclude = ['id']

"""
class BookSerializer(Serializer):
    title = CharField(max_length=255)
    pub_year = DateField()
    isbn = CharField(max_length=13)
    price = DecimalField(max_digits=19, decimal_places=2)
"""
class GenreSerializer(Serializer):
    name = CharField(max_length=255)
