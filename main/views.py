from django.shortcuts import render
from django.http import HttpResponse


def index(request) : 
    return render(request, 'main/index.html')

def about(request) :
    return HttpResponse("About us")

def tracker(request) :
    return HttpResponse("tracker page")

def search(request) :
    return HttpResponse("search")

def contact(request) :
    return HttpResponse("contact")

def checkout(request) :
    return HttpResponse("checkout")

def product_view(request) :
    return HttpResponse("product view")