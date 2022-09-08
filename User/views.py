from django.shortcuts import HttpResponse
from urllib import response
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.shortcuts import render,redirect
from .form import UserRegisterForm
from django.contrib.auth.models import User
import re
from cryptography.fernet import Fernet
import base64
import logging
import traceback
from django.conf import settings
from django.views.decorators.cache import cache_control
from .models import UserRegistration
from .form import UserLoginForm,uploadDocumentForm
from django.contrib.auth.models import User
from django.contrib import messages

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
# /^[a-zA-Z0-9.!#$%&’*+/=?^`{|}~-]+@([a-zA-Z0-9-]+[.]){1,2}[a-zA-Z]{2,10}$/
def isValid(email):
    if re.fullmatch(regex, email):
        print("Validemail")
        return "Validemail"
    else:
        print("Invalidemail")
        return "Invalidemail"


def encrypt(pas):
    try:        
        pas = str(pas)
        cipher_pass = Fernet(settings.ENCRYPT_KEY)
        encrypt_pass = cipher_pass.encrypt(pas.encode('ascii'))
        encrypt_pass = base64.urlsafe_b64encode(encrypt_pass).decode("ascii") 
        print("inside1",cipher_pass)
        print("inside2",encrypt_pass)
        return encrypt_pass
    except Exception as e:
        logging.getLogger("error_logger").error(traceback.format_exc())
        return None


def decrypt(pas):
    try:
        pas = base64.urlsafe_b64decode(pas)
        cipher_pass = Fernet(settings.ENCRYPT_KEY)
        decod_pass = cipher_pass.decrypt(pas).decode("ascii")     
        return decod_pass
    except Exception as e:
        logging.getLogger("error_logger").error(traceback.format_exc())
        return None

# # Create your views here.
# def index(request):
#     return HttpResponse("User Registered")


# Create your views here.
def index(request):
    return HttpResponse("User")

def login(request):
    if request.method == 'POST':
        print('inside post')
        form = UserLoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            print("username ",uname)
            print("password ",upass)
            UserRegister=UserRegistration.objects.get(userregistration_email_field=uname)
            print("get user",UserRegister)
            if decrypt(UserRegister.userregistration_password) == upass:
                user = User.objects.get(username=uname)
                print("user authenticated")
                auth_login(request, user)
                return redirect('home')
        else:
            return render(request, 'User/login.html',{'form':form})
    else:    
        form = UserLoginForm()
    return render(request, 'User/login.html',{'form':form})    


def register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        print("inside registeration")
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            print("form is valid")
            emailstatus=isValid(form.cleaned_data.get('username').lower())
            print("status",emailstatus)
            if emailstatus != 'Invalidemail':
                encryptpass= encrypt(form.cleaned_data.get('password1'))
                encryptconfirmpass= encrypt(form.cleaned_data.get('password2'))
                email = form.cleaned_data.get('username').lower()
                data=User(username=email, password=encryptpass)
                data.save()
                print("userpassword",data.password)
                createdresult=UserRegistration.objects.create(userregistration_email_field=email, userregistration_password=encryptpass, userregistration_confirm_password=encryptconfirmpass, registration_User_Type=form.cleaned_data.get('user_role'))
                if createdresult != '' or createdresult!= None:
                    print("userregitrationpassword",createdresult.userregistration_password)
                    print("user created")
                    return redirect('User:index')
                else:
                    print("User not created")
                    return redirect('User:register') 
            else:
                print("invalid")
                return redirect('User:register')
        else:
            print("form is not valid")
            messages.error(request, 'Error while processing your request')
            context = {
            'form': form
            }
            return render(request, 'User/register.html', context)
    else:
        print("inside registeration")
        context = {
            'form': form
        }
        return render(request, 'User/register.html',context)


def logout(request):
    auth_logout(request)
    return render(request, 'home.html')


def documenthub(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            print()
            form = uploadDocumentForm(request.POST, request.FILES)
            if form.is_valid():
                print("form is valid")
                form.save()
                messages.success(request, ('Your form is saved!'))
                return redirect('User:documenthub')
            else:
                print("form is not valid")
                context={
                    'form':form
                }
                messages.error(request, ('Your form is not saved!'))
                return render(request, 'User/documenthub.html',context)
        else:
            form=uploadDocumentForm()
            context={
                'form':form
            }
            return render(request, 'User/documenthub.html',context)
    else:
        return render(request, 'User/login.html')



def datatable(request):
    print('datatable')
    return render(request,'datatable.html')