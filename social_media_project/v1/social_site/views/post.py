from django.shortcuts import render, redirect


def post(request):
    return render(request, "v1/index.html")
