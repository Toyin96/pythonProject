from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.

def welcome(request):
    return HttpResponse("Welcome to the app section")
