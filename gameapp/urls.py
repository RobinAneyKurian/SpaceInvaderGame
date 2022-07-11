from django.urls import path 
from . import views

urlpatterns = [
    path("", views.game, name="game"),
    path("register", views.register, name='register'),
    path("home", views.home, name='home')
]