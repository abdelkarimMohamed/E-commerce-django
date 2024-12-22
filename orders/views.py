from django.shortcuts import render,get_object_or_404,redirect
from .models import OrderItem,Order
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
            return redirect('orders:pay_order',order_id=order.id)

        
        return render(request,'orders/created.html',{'order':order,'success':success})
    
    else:
        form=OrderCreateForm()
    return render(request,'orders/created.html',{'form':form,'cart':cart})

def order_pay_by_vodafone(request,order_id):
    
    order=get_object_or_404(Order,id=order_id)
    if request.method == 'POST':
        form=OrderPayForm(request.POST,request.FILES)
        if form.is_valid():
            
            order_pay=form.save(commit=False)
            # order.paid=True
            # order.save()
            # order_pay.paid=True
            order_pay.order=order
            order_pay.save()
            return redirect('orders:payment_success',order_id=order.id)
    else:
        form=OrderPayForm()

    context={'order':order,'form':form}
    return render(request,'orders/pay_form.html',context)

def payment_success(request,order_id):
    order=get_object_or_404(Order,id=order_id)
    return render(request,'orders/payment_success.html',{'order':order})
