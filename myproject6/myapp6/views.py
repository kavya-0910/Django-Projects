from django.shortcuts import render
from django.http import request,HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html')
def contact(request):
    return render(request,'contact.html')
def login(request):
    return render(request,'login.html')
def register(request):
    return render(request,'register.html')
def search(request):
    return render(request,'search.html')
def emphome(request):
    return render(request,'emphome.html')
def delete(request):
    return render(request,'delete.html')
def update(request):
    return render(request,'update.html')
def employeejpg(request):
    return render(request,'employee.jpg')
