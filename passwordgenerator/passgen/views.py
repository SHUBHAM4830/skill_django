from django.shortcuts import render
import random

def home(request):
    return render(request, 'passgen/home.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('number'):
        characters.extend(list('1234567890'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    length = int(request.GET.get('length', 8))  # Default to 8 if no length provided
    thepassword = ''.join(random.choice(characters) for _ in range(length))

    return render(request, 'passgen/password.html', {'thepassword': thepassword})
