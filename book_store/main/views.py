from django.http import Http404
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateAPIView)
from rest_framework.response import Response

from main.models import Author, Book, Genre
from main.serializers import AuthorSerializer, BookSerializer, GenreSerializer

class AuthorDetail(RetrieveUpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorList(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookView(APIView):
    def get(self, request):
        serializer = BookSerializer(Book.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        form = BookForm(request.data)
        if form.is_valid():
            book = form.save()
            return Response({'book_id': book.id})
        return Response({'error': form.errors})

class GenreDetail(RetrieveUpdateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreList(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

@require_http_methods(["GET", "POST"])
def book_detail(request, pk):
    try:
        book = Book.objects.get(id=pk)
    except Book.DoesNotExist:
        raise Http404("There is no such book unfortunately")
    return render(request, 'book.html', {'book': book})

@require_http_methods(["GET", "POST"])
def books_list(request):
    return render(request, 'books.html', {'books': Book.objects.all()})
