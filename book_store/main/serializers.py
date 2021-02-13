from rest_framework.serializers import ModelSerializer

from main.models import Author, Book, Genre

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
