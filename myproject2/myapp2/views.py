from django.shortcuts import render

# Create your views here.
from django.http import request, HttpResponse
def homepage(request):
    return HttpResponse("<h1>welcome to django web application</h1>")
def contactpage(request):
    return HttpResponse("<h1>welcome to contactpage</h1>")
def aboutpage(request):
    return HttpResponse("</h1>welcome to aboutpage</h1")
