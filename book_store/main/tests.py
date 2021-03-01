from locale import getdefaultlocale

from django.test import Client, TestCase

from factory import Factory, Faker, SubFactory

from main.models import Author, Book, Genre
from main.serializers import AuthorSerializer, BookSerializer, GenreSerializer

class AuthorFaker(Factory):
    class Meta:
        model = Author
    name = Faker('full_name', locale=getdefaultlocale()[0])
    birth_date = DateField(null=False, blank=False, db_column='birth_date',
        verbose_name='Дата рождения')
    death_date =

class GenreFaker(Factory):
    class Meta:
        model = Genre
    name = Faker('word', locale=getdefaultlocale()[0])

class BookFaker(Factory):
    class Meta:
        model = Movie

    title = Faker('sentence', nb_words=3, locale=getdefaultlocale()[0])
    year = Faker('year')
    genre = SubFactory(GenreFaker)

class MovieAPITest(TestCase):
    MAX_MOVIES_COUNT = 20

    def setUp(self):
        self.client = Client()
        self.movies = MovieFaker.create_batch(self.MAX_MOVIES_COUNT)
        for movie in self.movies:
            print(movie.title, movie.year, movie.genre)
            movie.genre.save()
            movie.save()

    def test_movies_get(self):
        response = self.client.get('/api/movies/')
        self.assertEqual(Movie.objects.count(), self.MAX_MOVIES_COUNT)
        self.assertEqual(response.status_code, 200)
        expected = {'movies': MovieSerializer(self.movies, many=True).data}
        self.assertEqual(response.json(), expected)

    def tearDown(self):
        pass
