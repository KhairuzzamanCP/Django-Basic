from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse ("this is first_app page")
def about(request):
    return HttpResponse ("this is about page")
def courses(request):
    return HttpResponse ("this is courses page")