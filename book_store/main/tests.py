from locale import getdefaultlocale

from django.test import Client, TestCase

from factory import Factory, Faker, SubFactory

from main.models import Author, Book, Genre
from main.serializers import AuthorSerializer, BookSerializer, GenreSerializer

class AuthorFaker(Factory):
    class Meta:
        model = Author
    full_name = Faker('full_name', locale=getdefaultlocale()[0])
    birth_date = Faker('full_name', locale=getdefaultlocale()[0])
    death_date = Faker('full_name', locale=getdefaultlocale()[0])

class GenreFaker(Factory):
    class Meta:
        model = Genre
    name = Faker('word', locale=getdefaultlocale()[0])

class BookFaker(Factory):
    class Meta:
        model = Book

    title = Faker('sentence', nb_words=3, locale=getdefaultlocale()[0])
    pub_year = Faker('year')
    isbn = Faker('isbn', separator='')
    price = Faker('pydecimal', positive=True)
    genres = SubFactory(GenreFaker)

class BookAPITest(TestCase):
    MAX_MOVIES_COUNT = 20

    def setUp(self):
        self.client = Client()
        self.books = BookFaker.create_batch(self.MAX_MOVIES_COUNT)
        for book in self.books:
            print(book.title, book.year, book.genre)
            book.genre.save()
            book.save()

    def test_books_get(self):
        response = self.client.get('/books/api/')
        self.assertEqual(Book.objects.count(), self.MAX_MOVIES_COUNT)
        self.assertEqual(response.status_code, 200)
        expected = BookSerializer(self.books, many=True).data
        self.assertEqual(response.json(), expected)

    def tearDown(self):
        pass
