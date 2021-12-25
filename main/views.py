from django.shortcuts import render
from django.http import HttpResponse
from .models import MainCarousel, OfferCarousel, Categories, Product
from math import ceil

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
    products = Product.objects.filter(category=category)
    num_of_products = len(products)
    num_of_rows = ceil(num_of_products/4)
    params = {'category' : category, 'products' : products, 'num_of_products' : num_of_products}
    return render(request, 'main/category_view.html', params)


def product_view(request, id) :
    product = Product.objects.filter(id=id)[0]
    return render(request, 'main/product_view.html', {'product' : product})