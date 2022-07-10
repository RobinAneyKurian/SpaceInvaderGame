from django.shortcuts import render
from .models import Destination
# Create your views here.

def game(request):

    gamehome = Destination()
    gamehome.img = 'gamelogo.png'
    return render(request, "game.html", {'gamehome': gamehome})