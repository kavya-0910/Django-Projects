from django.shortcuts import render

# Create your views here.
from django.http import request, HttpResponse
def homepage(request):
    rollnumber=4
    name="Keerthy"
    coursename="python"
    fee=180000
    return HttpResponse(
        f"My Roll Number={rollnumber}""<br>"
        f"My Name={name}""<br>"
        f"MY course Name={coursename}""<br>"
        f"Fee={fee}"
    )