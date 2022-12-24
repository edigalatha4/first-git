from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def amazon(request):
    return HttpResponse('<h1>Amazon is a shopping website</h1>')
