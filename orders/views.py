from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm,OrderPayForm
from cart.cart import Cart
from django.core.mail import send_mail
from django.conf import settings
from .tasks import send_emails

def order_create(request):
    cart=Cart(request)
    success=False
    if request.method == 'POST':
        form=OrderCreateForm(request.POST)
        if form.is_valid():
            order=form.save()
            for item in cart:
                OrderItem.objects.create(order=order,product=item['product'],price=item['price'],quantity=item['quantity'])           
            cart.clear()
            # order_id=order.order_id
            # send_emails.delay(order_id)
            subject='Order Confimation'
            message=f'Your order ID: {order.order_id} has been created successfully. \n\n Orderdetails:\n'
            for item in cart:
                product_name=item['product'].name
                message+=f'Product: {product_name}, Price: {item['price']}, Quantity: {item['quantity']}\n'
            email_from=settings.DEFAULT_FROM_EMAIL
            recipinet_list=[form.cleaned_data['email']]
            send_mail(subject,message,email_from,recipinet_list)
            success=True
        return render(request,'orders/created.html',{'order':order,'success':success})
    
    else:
        form=OrderCreateForm()
    return render(request,'orders/created.html',{'form':form,'cart':cart})

