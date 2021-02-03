from django.db.models import (CharField, CheckConstraint, DateField,
    DecimalField, F, Model, Q, UniqueConstraint)
from django.db.models.functions import Now, Trunc

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
                check=Q(pub_year=Trunc('pub_year', 'year',
                    output_field=DateField()), pub_year__lt=Now()),
                name='book_pub_year_check'),
            CheckConstraint(check=Q(isbn__regex=r'\d{13}'),
                name='book_isbn_check'),
            CheckConstraint(check=Q(price__gt=0), name='book_price_check'),
        ]

class Author(Model):
    full_name = CharField(max_length=255, null=False, db_column='full_name',
        verbose_name='Полное имя автора')
    birth_date = DateField(null=False, db_column='birth_date',
        verbose_name='Дата рождения')
    death_date = DateField(null=False, db_column='death_date',
        default='9999-12-31', verbose_name='Дата сметри')

    class Meta:
        db_table = "author"
        constraints = [
            UniqueConstraint(fields=['full_name', 'birth_date'],
                name='author_full_name_birth_date_key'),
            CheckConstraint(
                check=Q(full_name__regex=r'\w{2,} (\w{1,2}\. |\w{2,} )?\w{2,}'),
                name='author_full_name_check'),
            CheckConstraint(
                check=Q(birth_date__lt=F('death_date')),
                name='author_full_name_check'),
        ]
"""
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
