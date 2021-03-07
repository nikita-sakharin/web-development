from django.contrib.admin import ModelAdmin, TabularInline, site

from main.models import Author, Book, Genre, User

class AuthorAdmin(ModelAdmin):
    list_display = ('id', 'full_name', 'birth_date')
    list_filter = ('full_name', 'birth_date', 'death_date')

site.register(Author, AuthorAdmin)

class GenreAdmin(ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name',)

site.register(Genre, GenreAdmin)

class BookAuthorsInline(TabularInline):
    model = Book.authors.through

class BookGenresInline(TabularInline):
    model = Book.genres.through

class BookAdmin(ModelAdmin):
    list_display = ('id', 'title', 'pub_year')
    list_filter = ('title', 'pub_year', 'isbn', 'price')
    inlines = [
        BookAuthorsInline,
        BookGenresInline,
    ]
    exclude = ('authors', 'genres')

site.register(Book, BookAdmin)

class UserAdmin(ModelAdmin):
    pass

site.register(User, UserAdmin)
