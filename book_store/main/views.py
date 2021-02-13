from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import generics

from main.models import Author, Book, Genre
from main.serializers import AuthorSerializer, BookSerializer, GenreSerializer

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

def book_detail(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404("There is no such book unfortunately")
    return render(request, 'book.html', {'book': book})

def books(request):
    return render(request, 'books.html', {'books': Book.objects.all()})
"""
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Movie
from .serializers import MovieSerializer

class BookView(APIView):
    serializer_class = BookSerializer
    def get(self, request, format=None):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        form = BookForm(request.GET) # GET or POST ?
        if form.is_valid():
            course = form.save()
            return Response({'post_id': course.id})
        return Response({'error': form.errors})

    def post(self, request):
        return Response({'error': None, 'result': 'Книга успешно добавлена'})

class MovieView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response({'movies': serializer.data})

    def post(self, request):
        # ...
        return Response({'error': None, 'result': 'Фильм успешно добавлен'})
"""
