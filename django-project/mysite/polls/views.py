from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.

def polls(request):
    return render(request,"index.html")


def success_page(request):
    print("welcome to server")
    return HttpResponse("<h1>I am Success</h1>")
