from django.urls import path
from text import views


urlpatterns = [
    path('', views.homeView, name="home"),
]