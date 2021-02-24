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
from django.contrib.admin import site
from django.contrib.auth.decorators import login_required
from django.urls import include, path
from django.views.generic.base import TemplateView

from main.views import avatars, avatar_change

urlpatterns = [
    path('', include('main.urls'), name='main'),
    path('', login_required(TemplateView.as_view(template_name='home.html')),
        name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/avatars/<int:pk>.<str:ext>/', avatars),
    path('accounts/avatar_change/', avatar_change),
    path('admin/', site.urls),
    path('social/', include('social_django.urls', namespace='social')), # name ?
]
