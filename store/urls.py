from django.urls import path
from . import views

app_name="store"

urlpatterns=[
    path('',views.list_product,name='list_of_products')
]