from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'appGen/home.html')

def about(request):
    return render(request, 'appGen/aboutUs.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*)(_+'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length',12))

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'appGen/password.html', {'password':thepassword})