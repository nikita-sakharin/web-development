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
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path
from django.views.generic.base import TemplateView

from main.views import avatar_get, avatar_change

urlpatterns = [
    path('', include('main.urls'), name='main'),
    path('', login_required(TemplateView.as_view(template_name='home.html')),
        name='home'),
    path('accounts/', include('django.contrib.auth.urls')), # ?
    path('admin/', site.urls),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'),
        name='logout'),
    path('social/', include('social_django.urls', namespace='social')), # name ?
    path('user/avatar/<path:path>', avatar_get, name='avatar'),
    path('user/avatar_change/', avatar_change),
]
