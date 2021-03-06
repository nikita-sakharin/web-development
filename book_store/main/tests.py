from locale import getdefaultlocale
from unittest.mock import patch

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import Client, TestCase
from django.urls import reverse

from factory import Factory, Faker, Sequence, post_generation
import faker
from selenium.webdriver.firefox.webdriver import WebDriver

from book_store.settings import DEFAULT_FILE_STORAGE
from main.models import Author, Book, Genre, User
from main.serializers import BookSerializer

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
        self.user = User.objects.get_or_create(username='test_user')[0]
        self.client.force_login(self.user)
        self.books = []
        for _ in range(100):
            author = AuthorFaker.create()
            author.save()
            genre = GenreFaker.create()
            genre.save()
            book = BookFaker.create(authors=[author], genres=[genre])
            self.books.append(book)

    @patch(DEFAULT_FILE_STORAGE + '.save')
    def test_avatar_change(self, mock_save):
        avatar = F'{self.user.id}.png'
        mock_save.return_value = avatar
        with open('main/static/images/default_avatar.png', 'rb') as file:
            response = self.client.post('/accounts/avatar_change/',
                {'avatar': file})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.get(pk=self.user.id).avatar, avatar)
        mock_save.assert_called_once()
        self.assertEqual(mock_save.call_args.args[0], F'avatars/{avatar}')

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

class SeleniumTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(50)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        password = '0123456789ABCDEF'
        user = User.objects.get_or_create(username='test_user')[0]
        user.set_password(password)
        user.save()

        self.selenium.get(self.live_server_url + reverse('login'))
        username_input = self.selenium.find_element_by_name('username')
        username_input.send_keys(user.username)
        password_input = self.selenium.find_element_by_name('password')
        password_input.send_keys(password)
        # self.selenium.find_element_by_xpath('//input[@value="Login"]').click()
        self.selenium.find_element_by_xpath('//button').click()
