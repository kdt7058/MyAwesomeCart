from django.shortcuts import render
from django.http import HttpResponse
from math import ceil
from .models import Product, Contact


# Create your views here.

def index(request):
    products = Product.objects.all()
    # n = len(products)
    # nSlides = n // 4 + ceil((n / 4) - (n // 4))
    # params = {'no_of_slides': n, 'range': range(1, nSlides), 'product': products}
    # allProds = [[products,range(1, nSlides), nSlides],[products,range(1, nSlides), nSlides]]
    # params = {"allProds": allProds}

    allProds =[]
    catprods = Product.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {"allProds": allProds}
    return render(request, 'shop/index.html',params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    if request.method=="POST":
        name = request.POST.get('name','')
        phone = request.POST.get('contact', '')
        email = request.POST.get('email', '')
        message = request.POST.get('comment', '')
        contact_info = Contact(name=name, email=email, contact=phone, message=message)
        contact_info.save()
    return render(request, 'shop/contact.html')


def tracker(request):
    return render(request, 'shop/tracker.html')


def search(request):
    return render(request, 'shop/search.html')

def prodView(request,myid):
    #fetch product using id
    product = Product.objects.filter(id=myid)
    print(product)
    param = {'product': product[0]}
    return render(request, 'shop/productview.html',param )


def checkout(request):
    return render(request, 'shop/checkout.html')
