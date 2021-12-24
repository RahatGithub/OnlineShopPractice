from django.shortcuts import render
from django.http import HttpResponse
from .models import MainCarousel, OfferCarousel, Categories, Product


def index(request) : 
    main_images_collection = MainCarousel.objects.values('image')
    main_images = {item['image'] for item in main_images_collection}
    offer_images_collection = OfferCarousel.objects.values('image')
    offer_images = {item['image'] for item in offer_images_collection}
    category_images_collection = Categories.objects.values('image')
    category_images = {item['image'] for item in category_images_collection}
    # Try doing the same with the above cases 
    categories_collection = Categories.objects.all()
    categories = {item for item in categories_collection}

    params = {'main_images' : main_images, 'offer_images' : offer_images, 'category_images': category_images, 'categories' : categories}
    print(categories)
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


def category_view(request, id) :
    category = Categories.objects.filter(id=id)[0]
    print(category)

    return HttpResponse("category view")


def product_view(request, id) :
    return HttpResponse("product view")