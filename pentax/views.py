from django.shortcuts import render
from django.shortcuts import HttpResponse


def hello(request):
    return HttpResponse("You're on the right track")


def landing_page(request):
    return render(request, 'landing_page.html')
