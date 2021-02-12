from rest_framework.serializers import (CharField, DateField, DecimalField,
    Serializer)

class AuthorSerializer(Serializer):
    full_name = CharField(max_length=255)
    birth_date = DateField()
    death_date = DateField()

"""
from rest_framework.serializers import ModelSerializer
class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
"""

class BookSerializer(Serializer):
    title = CharField(max_length=255)
    pub_year = DateField()
    isbn = CharField(max_length=13)
    price = DecimalField(max_digits=19, decimal_places=2)

class GenreSerializer(Serializer):
    name = CharField(max_length=255)
