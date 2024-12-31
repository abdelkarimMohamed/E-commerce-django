from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Account
from django.core.mail import send_mail
from django.conf import settings

@receiver(post_save,sender=Account)
def send_welcome_email(sender,instance,created,**kwargs):
    if created:
        subject='Welcome to Django for all.'
        message=f'Hi {instance.username},  \n thanks yoy for creating an acount with us.'
        from_email=settings.DEFAULT_FROM_EMAIL
        mail_sent=send_mail(subject,message,from_email,[instance.email])


