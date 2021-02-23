from django.conf.settings import DEBUG
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateAPIView)

from main.forms import ChangeAvatarForm
from main.models import Author, Book, Genre
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

from django.http import FileResponse, HttpResponse

@login_required
@require_http_methods(['GET'])
def avatar_get(request):
    # return HttpResponse(request.user.avatar.read(), content_type="image/jpeg")
    if DEBUG:
        avatar = request.user.avatar
        return FileResponse(avatar)
    else:
        pass

@login_required
@require_http_methods(['GET', 'POST'])
def avatar_change(request):
    if request.method == 'POST':
        form = ChangeAvatarForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            user.avatar.delete()
            user.avatar = form.cleaned_data['avatar']
            # user.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = ChangeAvatarForm()
    return render(request, 'avatar_change.html', {'form': form})

@require_http_methods(["GET"])
def book_detail(request, pk):
    try:
        book = Book.objects.get(id=pk)
    except Book.DoesNotExist:
        raise Http404("There is no such book unfortunately")
    return render(request, 'book.html', {'book': book})

@require_http_methods(["GET"])
def book_list(request):
    return render(request, 'books.html', {'books': Book.objects.all()})
"""
curl -X POST -H "Content-Type: application/json" -d '{
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
