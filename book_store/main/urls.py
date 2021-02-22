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

from main.views import (BookDetail, BookList, avatar_detail, avatars_list,
    book_detail, book_list)

urlpatterns = [
    path('api/books/', BookList.as_view()),
    path('api/books/<int:pk>/', BookDetail.as_view()),
    path('books/', book_list, name='books-list'),
    path('books/<int:pk>/', book_detail, name='book-detail'),
    path('media/<int:user_id>/<filename>/', avatar_),
    path('media/<int:user_id>/', avatars_list),
]
# TODO BookSearch, BookSearchForm
