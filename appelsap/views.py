from django.shortcuts import render
from django.http import HttpResponse
from . import vars

# Create your views here.
def say_hello(request):
    return render(request, "hello.html", vars.dictio)

def home_page(request):
    return render(request, "index.html")

