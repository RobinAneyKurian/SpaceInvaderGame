import imp
from django.shortcuts import render, redirect
from .models import Destination
from django.contrib.auth.models import User, auth 
from django.contrib import messages
# Create your views here.

def game(request):

    gamehome = Destination()
    gamehome.img = 'gamelogo.png'
    return render(request, "game.html", {'gamehome': gamehome})


def register(request):

        if request.method == "POST":

            username = request.POST['username']
            email = request.POST['email']

            if User.objects.filter(username=username):
                messages.info(request,('Username Exists'))
                return redirect('register')
            elif User.objects.filter(email=email):
                messages.info(request, "Email Exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email)
                user.save()
                print("User Created")
            return redirect('/')



        else:
            return render(request, "register.html")

def home(request):
    return redirect('/')