from django.shortcuts import HttpResponse
from urllib import response
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("User")

def login(request):
    return render(request, 'User/login.html')


def register(request):
    return render(request, 'User/register.html')