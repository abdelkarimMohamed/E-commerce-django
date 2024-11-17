from django.contrib import admin
from .models import Account 

@admin.register(Account)
class AcountAdmin(admin.ModelAdmin):
    
    list_display=['first_name','email','user_name']
    search_fields=['user_name']