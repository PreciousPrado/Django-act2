from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, BSIT ")

def test(request):
    return HttpResponse("<a href='#'>Link<a/>")

def test2(request):
    return HttpResponse("<h1>Test 2<h1/>")
