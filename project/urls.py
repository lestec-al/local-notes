from django.contrib import admin
from django.urls import path, include
from text import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<slug:slug>/', views.otherView),
    path('', views.homeView, name="home"),
]
