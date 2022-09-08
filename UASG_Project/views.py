from django.shortcuts import HttpResponse
from urllib import response
from django.shortcuts import render
from User.models import DocumentHubData, DocumentHub_Languages, DocumentHub_Category


# Create your views here.


def home(request):
    return render(request, 'home.html')


def viewdocuments(request):
    DocumentHub_Data=DocumentHubData.objects.all()
    print("datata",DocumentHub_Data)
    context={
        'DocumentHub_Data':DocumentHub_Data
    }

    return render(request,'viewdocuments.html',context)