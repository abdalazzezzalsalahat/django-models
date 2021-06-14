from django.views.generic import HomeView, ListView, DetailView
from .models import Snacks


class SnacksListView(HomeView):
    template_name = "home.html"
    model = Snacks

class SnacksListView(ListView):
    template_name = "snacks_list.html"
    model = Snacks

class SnacksDetailView(DetailView):
    template_name = "snacks_detail.html"
    model = Snacks

