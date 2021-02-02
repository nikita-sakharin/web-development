from django.db import models

class Book(models.Model):
    title
    year
    isbn
    price

class Author(models.Model):
    full_name
    birth_date
    death_date

class Genre(models.Model):
    name
