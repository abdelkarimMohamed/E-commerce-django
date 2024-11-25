from django.db import models
# from django.contrib.auth.models import User
#AbstractBaseUser => to know django have usermodel maked custom
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager #responsible create  user
import pycountry

class MyAccountManager(BaseUserManager):

    def create_user(self, first_name, last_name, username,email, country, password=None):
        if not email:
            raise ValueError('User must have an email address.')
        if not username:
            raise ValueError('User must have an username.')
    
        user=self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            country=country,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, first_name, last_name,country,password):

        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            country=country,
            password=password,

        )
        user.is_admin=True
        user.is_active=True
        user.is_staff=True
        user.is_superadmin=True
        user.save(using=self._db)
        return user
    
class Account(AbstractBaseUser):

    @staticmethod
    def get_country():
        countries=list(pycountry.countries)
        country_choices=[(country.alpha_2,country.name) for country in countries]
        return country_choices
    
    first_name=models.CharField(max_length=250)
    last_name=models.CharField(max_length=250)
    email=models.EmailField(max_length=100,unique=True)
    username=models.CharField(max_length=100,unique=True)
    phone_number=models.CharField(max_length=50)
    country=models.CharField(max_length=2,choices=get_country(),default='US')

    date_joined=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now_add=True)

    is_active=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    is_superadmin=models.BooleanField(default=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username','first_name','last_name','country']

    objects=MyAccountManager()

    def __str__(self):
        return self.email
    
    def has_perm(self,perm,obj=None):  #check user if admin show dashboard inverse not show dashboard
        return self.is_superadmin
    
    def has_module_perms(self,app_label): #show all apps to any admin in dashboard
        return True
    
 