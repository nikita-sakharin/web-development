from django.shortcuts import render

def book_detail(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404("There is no such book unfortunately")
    # return render(request, 'book.html', {'book': book})
    return render(request, 'book.html', {'book': {
        'title': 'Война и Мир',
        'author': 'Лев николаевич Толстой',
        'year': 1867,
        'price': 3.99
    }})

def books(request):
    # return render(request, 'books.html', {'books': Book.objects.all()})
    return render(request, 'books.html', {'books': [
        {
            'title': 'Война и Мир',
            'author': 'Лев николаевич Толстой',
            'year': 1867,
            'price': 3.99
        },
        {
            'title': 'Introduction to Algorithms',
            'author': 'Thomas H. Cormen',
            'year': 2009,
            'price': 49.99
        }
    ]})
