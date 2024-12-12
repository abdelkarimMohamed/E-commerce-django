from django.contrib import admin
from .models import Order,OrderItem


class OrderItemInline(admin.TabularInline):   #TabularInline => OrderAdminيظهر تحت جدول ال 
    model=OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=['first_name','email','paid','created_at']
    inlines=[OrderItemInline]
