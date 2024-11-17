from django.shortcuts import render
from .forms import RegisterForm
from .models import Account

def register(request):
    
    if request.method == 'POST':
        form=RegisterForm(request.post)
        if form.is_valid():
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            email=form.cleaned_data['email']
            phone_number=form.cleaned_data['phone_number']
            country=form.cleaned_data['country']
            password=form.cleaned_data['password']
            user_name=email.split('@')[0]

            user=Account.objects.create_user(first_name=first_name,last_name=last_name,username=user_name,email=email,country=country,password=password)
            user.phone_number=phone_number
            user.save()