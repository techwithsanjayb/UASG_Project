from django.shortcuts import HttpResponse
from urllib import response
from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, 'home.html')


def viewdocuments(request):
    return render(request,'viewdocuments.html')