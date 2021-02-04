from django.shortcuts import render

def book_detail(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404("There is no such book unfortunately")
    return render(request, 'book.html', {'book': book})

def books(request):
    return render(request, 'books.html', {'books': Book.objects.all()})
