from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'passgenerator/home.html')

def password(request):
    char = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('upper'):
        char.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        char.extend(list('!@#$%^&*()'))

    if request.GET.get('numbers'):
        char.extend(list('1234567890'))

    length =  int(request.GET.get('length',8))

    thepass = ''
    
    for x in range(length):
        thepass += random.choice(char)

    return render(request, 'passgenerator/password.html', {'password': thepass})

def about(request):
    names = 'Hardian Permana Putra'
    bod = 'Jakarta, 08 Juli 1993'
    asa = 'Web Developer'
    company = 'PT Binabusana Internusa (Triputra Groups)'

    return render(request, 'passgenerator/about.html', {
        'names': names,
        'bod': bod,
        'as': asa,
        'company': company
    })