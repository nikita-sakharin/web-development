from django.contrib.admin import ModelAdmin

from main.models import Author, Book, Genre

class AuthorAdmin(ModelAdmin):
    list_display = ('id', 'full_name', 'birth_date')

admin.site.register(Author, AuthorAdmin)

class BookAdmin(ModelAdmin):
    list_display = ('id', 'title', 'pub_year')

admin.site.register(Book, BookAdmin)

class GenreAdmin(ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Genre, GenreAdmin)

class UserCourseAdmin(ModelAdmin):
    list_display = ('id', 'course_id_id', 'user_id_id')
    pass

admin.site.register(UserCourse, UserCourseAdmin)
