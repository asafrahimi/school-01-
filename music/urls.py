from django.shortcuts import render
from . import views
from django.http import HttpResponse
from django.conf.urls import url
# Create your views here.

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
