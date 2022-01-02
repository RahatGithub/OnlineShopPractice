from django.shortcuts import render
from django.http import HttpResponse
from .models import MainCarousel, OfferCarousel, Categories, Product , Contact, Cont_info
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


def contact(request):
    
    thank=False
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank=True
    
    emails_collection = Cont_info.objects.values('email')
    emails = {item['email'] for item in emails_collection}
    
    return render(request, 'main/contact.html', {'thank':thank, 'emails':emails})


def checkout(request) :
    return HttpResponse("checkout")


def category_view(request, id) :
    category = Categories.objects.filter(id=id)[0]
    products = Product.objects.filter(category=category) 
    params = {'category' : category, 'products' : products}
    return render(request, 'main/category_view.html', params)


def product_view(request, id) :
    product = Product.objects.filter(id=id)[0]
    return render(request, 'main/product_view.html', {'product' : product})