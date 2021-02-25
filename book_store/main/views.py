from os.path import splitext

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, HttpResponseForbidden
from django.shortcuts import (get_object_or_404, get_list_or_404, redirect,
    render)
from django.views.decorators.http import require_http_methods

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from main.forms import ChangeAvatarForm
from main.models import Author, Book, Genre, User
from main.serializers import AuthorSerializer, BookSerializer, GenreSerializer

class AuthorDetail(RetrieveUpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorList(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookDetail(RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookList(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class GenreDetail(RetrieveUpdateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreList(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

@login_required
@require_http_methods(['GET'])
def avatars(request, pk, ext):
    user = request.user
    if user.id != pk:
        if not user.is_staff:
            return HttpResponseForbidden('<!DOCTYPE html><html lang="en"><body>'
                '<h1>403 Forbidden</h1></body></html>')
        user = get_object_or_404(User, pk=pk)
    if not user.avatar.name.endswith(ext)
        raise Http404('404 Not Found')
    if user.avatar:
        return FileResponse(user.avatar)

@login_required
@require_http_methods(['GET', 'POST'])
def avatar_change(request):
    if request.method == 'POST':
        form = ChangeAvatarForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            user.avatar.delete()
            avatar = form.cleaned_data['avatar']
            avatar.name += '.' + avatar.content_type.split('/')[-1]
            user.avatar = avatar
            user.save()
            return redirect('home')
    else:
        form = ChangeAvatarForm()
    return render(request, 'avatar_change.html', {'form': form})

@require_http_methods(["GET"])
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book.html', {'book': book})

@require_http_methods(["GET"])
def book_list(request):
    return render(request, 'books.html', {'books': get_list_or_404(Book)})
"""
curl -X POST -H 'Content-Type: application/json' -d '{
    "title": "Основы математического анализа",
    "pub_year": "2021-01-01",
    "isbn": "9785811475834",
    "price": 1460,
    "authors": [
        2
    ],
    "genres": [
        3
    ]
}' http://127.0.0.1:8000/api/books/
"""
