from django.shortcuts import render
from django.http import HttpResponse
from .models import MainCarousel, OfferCarousel


def index(request) : 
    main_images_collection = MainCarousel.objects.values('image')
    main_images = {item['image'] for item in main_images_collection}

    offer_images_collection = OfferCarousel.objects.values('image')
    offer_images = {item['image'] for item in offer_images_collection}

    params = {'main_images' : main_images, 'offer_images' : offer_images}

    return render(request, 'main/index.html', params)

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