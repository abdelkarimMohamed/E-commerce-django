from django.shortcuts import render,get_object_or_404
from .models import Category,Product



def list_product(request,category_slug=None):

    category=None
    categories=Category.objects.all()
    products=Product.objects.filter(status=Product.Status.AVAILABLE)

    if category_slug:

        category=get_object_or_404(Category,slug=category_slug)
        products=products.filter(category=category)

    context={
        'products':products,
        'category':category,
        'categories':categories,
    }
    return render(request,'store/list_products.html',context)

def product_detail(request,product_slug):


    product=get_object_or_404(Product,slug=product_slug,status=Product.Status.AVAILABLE)

    context={
        'detail':product
    }
    return render(request,'store/product_detail.html',context)