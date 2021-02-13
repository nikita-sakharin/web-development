"""book_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from main.views import BookDetail, BookList, book_detail, books

urlpatterns = [
    path('api/books/', BookList.as_view()),
    path('api/books/<int:pk>/', BookDetail.as_view()),
    path('books/<int:book_id>', book_detail, name='book_detail'),
    path('books', books, name='books'),
]
# TODO декоратор
# POST - добавление update.
# PUT добавление
# всё в виде json!!!!
