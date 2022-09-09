from dataclasses import fields
from logging import PlaceHolder
from pyexpat import model
from tkinter import Widget
from xml.dom import ValidationErr
from django import forms
from django.core import validators
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import DocumentHubData




class UserRegisterForm(UserCreationForm):
    username = forms.EmailField(
        max_length=60,
        required=True,
        help_text='Enter Email',
        widget=forms.TextInput(attrs={'class': 'form-control input-1', 'autocomplete':'off'})
    )
    password1 = forms.CharField(
        max_length=500,
        help_text='Enter Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control input-1', 'autocomplete':'off'}),
    )

    password2 = forms.CharField(
        max_length=500,
        required=True,
        help_text='Enter Confirm Password',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control input-1', 'autocomplete':'off'}),
    )     
    
    CHOICES = [('Individual', 'Individual'),
               ('Organization', 'Organization'),
               ('DomainExpert', 'DomainExpert')] 

    user_role = forms.ChoiceField(validators=[validators.MaxLengthValidator(20)], required=True, help_text='Select User Role',
                                 choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control input-1','autocomplete':'off'}),)

    class Meta:
        model = User
        fields = [
            'username', 'password1', 'password2', 'user_role',
        ]




class UserLoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.EmailField(validators=[validators.EmailValidator(), validators.MaxLengthValidator(
        50)], widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email','autocomplete':'off'}), required=True)
        
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
                'autocomplete':'off',
               

            }
        ))


class uploadDocumentForm(forms.ModelForm):
    class Meta:
        model = DocumentHubData
        fields = ('DocumentHubData_Title', 'DocumentHubData_CategoryType', 'DocumentHubData_FileSize','DocumentHubData_Tags', 'DocumentHubData_UploadSupportDocument', 'DocumentHubData_DownloadCounter','DocumentHubData_PublishedStatus','DocumentHubData_Languages','DocumentHubData_Author')


