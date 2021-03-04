from locale import getdefaultlocale

from django.test import Client, TestCase

from factory import Factory, Faker, Sequence, SubFactory, post_generation
import faker

from main.models import Author, Book, Genre
from main.serializers import AuthorSerializer, BookSerializer, GenreSerializer

UNIQUE_FAKER = faker.Faker(locale=getdefaultlocale()[0]).unique

class AuthorFaker(Factory):
    class Meta:
        model = Author
    full_name = Faker('name', locale=getdefaultlocale()[0])
    birth_date = Faker('date_of_birth')

class GenreFaker(Factory):
    class Meta:
        model = Genre
    name = Sequence(lambda _: UNIQUE_FAKER.word())

class BookFaker(Factory):
    class Meta:
        model = Book

    title = Faker('sentence', nb_words=3, locale=getdefaultlocale()[0])
    pub_year = Faker('date', pattern='%Y-01-01')
    isbn = Sequence(lambda _: UNIQUE_FAKER.isbn13(separator=''))
    price = Faker('pydecimal', positive=True, min_value=1)

    @post_generation
    def authors(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        self.save()
        for author in extracted:
            self.authors.add(author)

    @post_generation
    def genres(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        self.save()
        for genre in extracted:
            self.genres.add(genre)

class BookAPITest(TestCase):
    def setUp(self):
        self.client = Client()
        self.books = []
        for _ in range(100):
            author = AuthorFaker.create()
            author.save()
            genre = GenreFaker.create()
            genre.save()
            book = BookFaker.create(authors=[author], genres=[genre])
            self.books.append(book)

    def test_book_detail(self):
        for book in self.books:
            response = self.client.get(F'/api/books/{book.id}/')
            self.assertEqual(response.status_code, 200)
            data = BookSerializer(book).data
            self.assertCountEqual(response.json(), data)

    def test_book_list(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, 200)
        data = BookSerializer(self.books, many=True).data
        self.assertCountEqual(response.json(), data)

    def tearDown(self):
        pass
