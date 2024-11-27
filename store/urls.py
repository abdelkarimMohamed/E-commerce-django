from django.urls import path
from . import views

app_name="store"

urlpatterns=[
    path('',views.list_product,name='list_of_products'),
    path('<slug:product_slug>/',views.product_detail,name='product_detail'),
]