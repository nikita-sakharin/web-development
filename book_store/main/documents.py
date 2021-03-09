from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry

from main.models import Book, User

@registry.register_document
class BookDocument(Document):
    class Index:
        name = 'books'
        settings = {'number_of_shards': 1, 'number_of_replicas': 0}

    class Django:
        model = Book
        fields = [
            'title',
            'pub_year',
            'isbn',
            # 'authors__full_name',
            # 'genres__name'
        ]

@registry.register_document
class UserDocument(Document):
    class Index:
        name = 'users'
        settings = {'number_of_shards': 1, 'number_of_replicas': 0}

    class Django:
        model = User
        fields = [
            'email',
            'first_name'
            'last_name',
            'username',
        ]
