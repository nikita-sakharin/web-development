from django.forms import Form, ImageField, ModelForm

from main.models import Author, Book, Genre

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        exclude = ['id']

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        exclude = ['id']

class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'
        exclude = ['id']

class UploadAvatarForm(Form):
    avatar = ImageField()
