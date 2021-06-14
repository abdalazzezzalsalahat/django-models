from django.urls import path
from .views import SnacksHomeView, SnacksListView, SnacksDetailView


urlpatterns = [
    path('', SnacksHomeView.as_view(), name="home"),
    path('list', SnacksListView.as_view(), name="snacks_list"),
    path('<int:pk>/', SnacksDetailView.as_view(), name="snacks_detail"),
]

