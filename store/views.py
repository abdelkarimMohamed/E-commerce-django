from django.shortcuts import render
from .models import Category,Product



def list_product(request):

    products=Product.objects.filter(status=Product.Status.AVAILABLE)
    context={
        'products':products
    }
    return render(request,'store/list_products.html',context)