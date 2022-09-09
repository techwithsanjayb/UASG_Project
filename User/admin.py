from django.contrib import admin
from .models import UserRegistration,DocumentHub_Category,DocumentHubData,DocumentHub_Languages
# Register your models here.

admin.site.register(UserRegistration)

admin.site.register(DocumentHub_Category)

admin.site.register(DocumentHubData)

admin.site.register(DocumentHub_Languages)