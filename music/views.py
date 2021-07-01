from django.shortcuts import render
from . import views
from django.http import HttpResponse
# Create your views here.

def index(request):
    pumi = " vivi"
    return HttpResponse("<h1>This is the music"+pumi+" app homepage</h1>")

#def index(request)=
#    ("Car": "Suzuki"})
