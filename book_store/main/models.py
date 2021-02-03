from django.db.models import (CharField, CheckConstraint, DateField,
    DecimalField, F, Model, Q)
from django.db.models.functions import Now

class Book(Model):
    title = CharField(max_length=255, null=False, db_column='title',
        verbose_name='Заглавие книги')
    pub_year = DateField(null=False, db_column='pub_year',
        verbose_name='Год публикации')
    isbn = CharField(max_length=13, null=False, db_column='isbn', unique=True,
        verbose_name='Международный стандартный номер книги')
    price = DecimalField(max_digits=19, decimal_places=2, null=False,
        db_column='price', verbose_name='Цена')

    class Meta:
        db_table = "book"
        constraints = [
            CheckConstraint(check=~Q(title=''), name='book_title_check'),
            CheckConstraint(
                check=Q(pub_year__year=F('pub_year'), pub_year__le=Now()),
                name='book_pub_year_check'),
            CheckConstraint(check=Q(isbn__regex=r'\d{13}'),
                name='book_isbn_check'),
            CheckConstraint(check=Q(price__gt=0), name='book_price_check'),
        ]
"""
class Author(Model):
    fullName = CharField(255, null=False, db_column='full_name')
    birthDate = DateField(db_column='birth_date')
    deathDate = DateField(null=False, db_column='death_date',
        default='9999-12-31')

    class Meta:
        db_table = "author"
        managed = False
        constraints = [
        CheckConstraint(check=~Q(team_home=F('team_visitors')), name='team_home_and_team_visitors_can_not_be_equal')
            UniqueConstraint(fields=['full_name', 'birth_date'], name='')
        ]

class Author(Model):
    full_name = CharField(max_length=255)
    birth_date = DateField()
    death_date = DateField()

    class Meta:
        managed = False
        db_table = 'author'
        unique_together = (('full_name', 'birth_date'),)


class Book(Model):
    title = CharField(max_length=255)
    year = DateField()
    isbn = CharField(unique=True, max_length=13)
    price = TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'book'


class BookAuthor(Model):
    book = ForeignKey(Book, DO_NOTHING)
    author = ForeignKey(Author, DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'book_author'
        unique_together = (('book', 'author'),)


class BookGenre(Model):
    book = ForeignKey(Book, DO_NOTHING)
    genre = ForeignKey('Genre', DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'book_genre'
        unique_together = (('book', 'genre'),)


class Genre(Model):
    name = CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'genre'
"""
