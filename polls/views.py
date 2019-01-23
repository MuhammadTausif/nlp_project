from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is again a request")

def index1(request):
    return HttpResponse("1")

def index2(request):
    return HttpResponse("2")

def index3(request):
    return HttpResponse("3++")