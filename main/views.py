from django.shortcuts import render
from django.http import HttpResponse
from .models import MainCarousel, OfferCarousel, Categories, Product , Contact, Cont_info, Dynamic_Product, Order, OrderUpdate
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

    dynamicProds = []
    productCaptions = Dynamic_Product.objects.values('caption', 'id')
    captions = {item['caption'] for item in productCaptions}
    for caption in captions :
        prod = Dynamic_Product.objects.filter(caption=caption)
        dynamicProds.append(prod)

    params = {
        'main_images' : main_images, 
        'offer_images' : offer_images, 
        'category_images': category_images, 
        'categories' : categories, 
        'dynamicProds' : dynamicProds
    }

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
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')  
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Order(items_json=items_json, name=name, amount=amount, email=email, address=address, city=city, zip_code=zip_code, phone=phone)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        thank = True
        id = order.order_id
        print(items_json)
        return render(request, 'main/checkout.html', {'thank':thank, 'id': id})
    return render(request, 'main/checkout.html')


def category_view(request, id) :
    category = Categories.objects.filter(id=id)[0]
    products = Product.objects.filter(category=category) 
    params = {'category' : category, 'products' : products}
    return render(request, 'main/category_view.html', params)


def product_view(request, id) :
    product = Product.objects.filter(id=id)[0]
    return render(request, 'main/product_view.html', {'product' : product})

# tried with code instead of id
# def product_view(request, code) :
#     product = Product.objects.filter(code=code)[0]
#     return render(request, 'main/product_view.html', {'product' : product})


def dynamic_product_view(request, id) :
    product = Dynamic_Product.objects.filter(id=id)[0]
    return render(request, 'main/product_view.html', {'product' : product})