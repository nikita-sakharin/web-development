from django.contrib.admin import ModelAdmin, site

from main.models import Author, Book, Genre

class AuthorAdmin(ModelAdmin):
    list_display = ('id', 'full_name', 'birth_date')
    list_filter = ('full_name', 'birth_date', 'death_date')

site.register(Author, AuthorAdmin)

class BookAdmin(ModelAdmin):
    list_display = ('id', 'title', 'pub_year')
    list_filter = ('title', 'pub_year', 'isbn', 'price')

site.register(Book, BookAdmin)

class GenreAdmin(ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name',)

site.register(Genre, GenreAdmin)
"""
class BookAuthorAdmin(ModelAdmin):
    list_display = ('id', 'course_id_id', 'user_id_id')

site.register(BookAuthor, BookAuthorAdmin)
"""
