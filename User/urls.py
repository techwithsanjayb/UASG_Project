from django.urls import path
from . import views

app_name='User'

urlpatterns = [   
    path('',views.index,name="index" ),
    path('login',views.login,name="login"),
    path('register', views.register, name="register"),
    path('uploaddocumenthub',views.documenthub, name="documenthub"),
    path('datatable',views.datatable, name="datatable")
    path('logout', views.logout, name="logout"),
]