from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def about(request):
    return httpresponse("welcome to about page")

def dynamic(request,roll):
    return httpresponse(f"Hello {roll}")

def dynamic2(request,roll):
    return httpresponse(f"Hello {roll}")


