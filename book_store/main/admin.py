from django.contrib.admin import ModelAdmin, TabularInline, site

from main.models import Author, Book, Genre

class BookAuthorsInline(TabularInline):
    model = Book.authors.through

class AuthorAdmin(ModelAdmin):
    list_display = ('id', 'full_name', 'birth_date')
    list_filter = ('full_name', 'birth_date', 'death_date')
    inlines = [
        BookAuthorsInline,
    ]

site.register(Author, AuthorAdmin)

class BookGenresInline(TabularInline):
    model = Book.genres.through

class GenreAdmin(ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name',)
    inlines = [
        BookGenresInline,
    ]

site.register(Genre, GenreAdmin)

class BookAdmin(ModelAdmin):
    list_display = ('id', 'title', 'pub_year')
    list_filter = ('title', 'pub_year', 'isbn', 'price')
    inlines = [
        BookAuthorsInline,
        BookGenresInline,
    ]
    exclude = ('authors', 'genres')

site.register(Book, BookAdmin)
