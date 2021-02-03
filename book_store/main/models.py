from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255, null=False,
        db_column='title', verbose_name='Заглавие книги')
    year = models.DateField(null=False, db_column='year',
        verbose_name='Год публикации')
    isbn = models.CharField(max_length=13, null=False, db_column='isbn',
        unique=True, verbose_name='Международный стандартный номер книги')
    price = models.DecimalField(max_digits=19, decimal_places=2,
        null=False, db_column='price', verbose_name='Цена')

    class Meta:
        db_table = "book"
        constraints = [
            models.CheckConstraint(check=~Q(title=''), name='book_title_check'),
            models.CheckConstraint(check=Q(year=''), name='book_title_check'),
            pub_date__year=2005
        ]
ndexes:
    "book_pkey" PRIMARY KEY, btree (id)
    "book_isbn_key" UNIQUE CONSTRAINT, btree (isbn)
Check constraints:
    "book_isbn_check" CHECK (isbn ~ similar_escape('\d{13}'::text, NULL::text))
    "book_price_check" CHECK (price > 0::money)
    "book_title_check" CHECK (title::text <> ''::text)
    "book_year_check" CHECK (year = date_trunc('year'::text, year::timestamp with time zone) AND year < CURRENT_DATE)
Referenced by:
    TABLE "book_author" CONSTRAINT "book_author_book_id_fkey" FOREIGN KEY (book_id) REFERENCES book(id)
    TABLE "book_genre" CONSTRAINT "book_genre_book_id_fkey" FOREIGN KEY (book_id) REFERENCES book(id)
"""
class Author(models.Model):
    fullName = models.CharField(255, null=False, db_column='full_name')
    birthDate = models.DateField(db_column='birth_date')
    deathDate = models.DateField(null=False, db_column='death_date',
        default='9999-12-31')

    class Meta:
        db_table = "author"
        managed = False
        constraints = [
        models.CheckConstraint(check=~Q(team_home=F('team_visitors')), name='team_home_and_team_visitors_can_not_be_equal')
            models.UniqueConstraint(fields=['full_name', 'birth_date'], name='')
        ]

class Genre(models.Model):
    name






class Author(models.Model):
    full_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    death_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'author'
        unique_together = (('full_name', 'birth_date'),)


class Book(models.Model):
    title = models.CharField(max_length=255)
    year = models.DateField()
    isbn = models.CharField(unique=True, max_length=13)
    price = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'book'


class BookAuthor(models.Model):
    book = models.ForeignKey(Book, models.DO_NOTHING)
    author = models.ForeignKey(Author, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'book_author'
        unique_together = (('book', 'author'),)


class BookGenre(models.Model):
    book = models.ForeignKey(Book, models.DO_NOTHING)
    genre = models.ForeignKey('Genre', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'book_genre'
        unique_together = (('book', 'genre'),)


class Genre(models.Model):
    name = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'genre'
"""
