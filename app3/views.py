from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def chicken(request):
    return HttpResponse('<b><h1>When in dout chicken is out</h1></b>')
