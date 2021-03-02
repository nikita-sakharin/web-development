from locale import getdefaultlocale

from django.test import Client, TestCase

from factory import Factory, Faker, SubFactory, post_generation

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
    pub_year = Faker('date_object')
    isbn = Faker('isbn13', separator='')
    price = Faker('pydecimal', positive=True)

    @post_generation
    def genres(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        for genre in extracted:
            self.genres.add(genre)

class BookAPITest(TestCase):
    def setUp(self):
        self.client = Client()
        self.books = BookFaker.create_batch(100)
        for book in self.books:
            book.pub_year = book.pub_year.replace(day=1, month=1)
            # book.genre.save()
            book.save()

    def test_books_get(self):
        response = self.client.get('/api/books/')
        self.assertEqual(Book.objects.count(), len(self.books))
        self.assertEqual(response.status_code, 200)
        expected = BookSerializer(self.books, many=True).data
        self.assertEqual(response.json(), expected)

    def tearDown(self):
        pass
