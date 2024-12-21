import time
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import Order


@shared_task
def send_emails(order_id):

    order=Order.objects.get(order_id=order_id)
    subject=f'Order ID:{order.order_id}'
    message=f'Dear {order.first_name} {order.last_name}, \n you have successfully placed an order. \n Your Order ID Is:{order.order_id}'
    from_email=settings.DEFAULT_FROM_EMAIL
    mail_sent=send_mail(subject,message,from_email,[order.email])
    return mail_sent