from django.shortcuts import HttpResponse
from urllib import response
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
# Create your views here.
def index(request):
    return HttpResponse("User")

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            print(user)
            if user is not None:
              return redirect('register')
        else:
            return render(request, 'User/login.html',{'form':form})
    else:    
        form = AuthenticationForm()
        return render(request, 'User/login.html',{'form':form})


def register(request):
    return render(request, 'User/register.html')