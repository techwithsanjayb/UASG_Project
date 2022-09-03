from django.shortcuts import HttpResponse
from urllib import response
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'Discussion_Forum/index.html')