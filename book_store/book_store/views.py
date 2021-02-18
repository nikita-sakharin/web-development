from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView

@login_required
class HomePageView(TemplateView):
    template_name = 'home.html'
