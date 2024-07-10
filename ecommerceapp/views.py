from django.shortcuts import render
from ecommerceapp.models import Contact,Product
from django.contrib import messages
import math
# Create your views here.


def index(request):
    allProds = []
    catProds = Product.objects.values('category','id')
    cats = {item['category'] for item in catProds}
    for cat in cats:
        prod = Product.objects.filter(category = cat)
        n = len(prod)
        nSlides = n // 4 + math.ceil((n/4)-(n//4))
        allProds.append([prod,range(1,nSlides),nSlides])

    params = {'allProds':allProds}
    return render(request,'index.html',params)




def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        pnumber = request.POST.get('pnumber')
        myquery = Contact(name = name,email = email,desc = desc,phonenumber = pnumber)
        myquery.save()
        messages.info(request,"We will get back you soon...")
    return render(request,'contact.html')


def checkout(request):
    return render(request,'checkout.html')


def about(request):
    pass