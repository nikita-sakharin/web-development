from django.db.models import (CharField, CheckConstraint, DateField,
    DecimalField, F, ManyToManyField, Model, Q, UniqueConstraint)
from django.db.models.functions import Now, Trunc

class Author(Model):
    full_name = CharField(max_length=255, null=False, db_column='full_name',
        verbose_name='Полное имя автора')
    birth_date = DateField(null=False, db_column='birth_date',
        verbose_name='Дата рождения')
    death_date = DateField(null=False, db_column='death_date',
        default='9999-12-31', verbose_name='Дата сметри')

    def __str__(self) -> str:
        if str(self.death_date) == '9999-12-31':
            return F'{self.full_name}: {self.birth_date}'
        return F'{self.full_name}: {self.birth_date} - {self.death_date}'

    class Meta:
        db_table = 'author'
        constraints = [
            UniqueConstraint(fields=['full_name', 'birth_date'],
                name='author_full_name_birth_date_key'),
            CheckConstraint(
                check=Q(full_name__regex=r'\w{2,} (\w{1,2}\. |\w{2,} )?\w{2,}'),
                name='author_full_name_check'),
            CheckConstraint(
                check=Q(birth_date__lt=F('death_date')),
                name='author_check'),
        ]

class Genre(Model):
    name = CharField(max_length=255, null=False, db_column='name', unique=True,
        verbose_name='Название жанра')

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'genre'
        constraints = [
            CheckConstraint(check=~Q(name=''), name='genre_name_check'),
        ]

class Book(Model):
    title = CharField(max_length=255, null=False, db_column='title',
        verbose_name='Заглавие книги')
    pub_year = DateField(null=False, db_column='pub_year',
        verbose_name='Год публикации')
    isbn = CharField(max_length=13, null=False, db_column='isbn', unique=True,
        verbose_name='Международный стандартный номер книги')
    price = DecimalField(max_digits=19, decimal_places=2, null=False,
        db_column='price', verbose_name='Цена')
    author = ManyToManyField(Author)
    genre = ManyToManyField(Genre)

    def __str__(self) -> str:
        return F'{self.title}, {self.pub_year.year} - {self.isbn}'

    class Meta:
        db_table = 'book'
        constraints = [
            UniqueConstraint(fields=['title', 'pub_year'],
                name='book_title_pub_year_key'),
            CheckConstraint(check=~Q(title=''), name='book_title_check'),
            CheckConstraint(
                check=Q(pub_year=Trunc('pub_year', 'year',
                    output_field=DateField()), pub_year__lt=Now()),
                name='book_pub_year_check'),
            CheckConstraint(check=Q(isbn__regex=r'\d{13}'),
                name='book_isbn_check'),
            CheckConstraint(check=Q(price__gt=0), name='book_price_check'),
        ]
"""
from main.models import Author, Book, Genre

Author(full_name='Александр Сергеевич Пушкин', birth_date='1799-06-06',
    death_date='1837-02-10').save()
Author(full_name='Григорий Михайлович Фихтенгольц', birth_date='1888-06-05',
    death_date='1959-06-26').save()
Author(full_name='Лев Николаевич Толстой', birth_date='1828-09-09',
    death_date='1910-11-20').save()
Author(full_name='Фёдор Михайлович Достоевский', birth_date='1821-11-11',
    death_date='1881-02-09').save()

Author(full_name='Клиффорд Штайн', birth_date='1965-12-14').save()
Author(full_name='Рональд Линн Ривест', birth_date='1947-01-01').save()
Author(full_name='Томас Х. Кормен', birth_date='1956-01-01').save()
Author(full_name='Чарльз Эрик Лейзерсон', birth_date='1953-11-10').save()

Genre(name='Драма').save()
Genre(name='Компьютерные науки').save()
Genre(name='Математика').save()
Genre(name='Роман').save()

Book(title='Алгоритмы: построение и анализ', pub_year='1990-01-01',
    isbn='9785845920164', price=5500).save()
Book(title='Анна Каренина', pub_year='1875-01-01',
    isbn='9785170878888', price=222).save()
Book(title='Борис Годунов', pub_year='1831-01-01',
    isbn='9785040978076', price=136).save()
Book(title='Война и мир', pub_year='1865-01-01',
    isbn='9785389071230', price=297).save()
Book(title='Евгений Онегин', pub_year='1825-01-01',
    isbn='9785170931217', price=190).save()
Book(title='Курс дифференциального и интегрального исчисления',
    pub_year='1947-01-01', isbn='9785811470617', price=2995).save()
Book(title='Преступление и наказание', pub_year='1866-01-01',
    isbn='9785170906307', price=176).save()

Book.objects.get(id=1).author.add(5)
Book.objects.get(id=1).author.add(6)
Book.objects.get(id=1).author.add(7)
Book.objects.get(id=1).author.add(8)
Book.objects.get(id=2).author.add(3)
Book.objects.get(id=3).author.add(1)
Book.objects.get(id=4).author.add(3)
Book.objects.get(id=5).author.add(1)
Book.objects.get(id=6).author.add(2)
Book.objects.get(id=7).author.add(4)

Book.objects.get(id=1).genre.add(2)
Book.objects.get(id=2).genre.add(4)
Book.objects.get(id=3).genre.add(1)
Book.objects.get(id=4).genre.add(4)
Book.objects.get(id=5).genre.add(4)
Book.objects.get(id=6).genre.add(3)
Book.objects.get(id=7).genre.add(4)
"""
