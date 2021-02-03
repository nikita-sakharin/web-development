from django.db import models

class Book(models.Model):
    title = models.CharField('Заглавие книги', max_length=255, null=False, db_column='title')
    year = models.DateField('Год публикации', null=False, db_column='year')
    isbn = models.CharField('Международный стандартный номер книги', max_length=13, null=False, db_column='isbn', unique=True)
    price = models.DecimalField(max_digits=19, decimal_places=2,
        null=False, db_column='price')

class Author(models.Model):
    fullName = models.CharField(255, null=False, db_column='full_name')
    birthDate = models.DateField(db_column='birth_date')
    deathDate = models.DateField(db_column='death_date', default=)

class Genre(models.Model):
    name
