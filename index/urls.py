from django.contrib import admin
from django.urls import path
from index.views import index
from user.views import login

urlpatterns = [
    path('', index, name='index')
]