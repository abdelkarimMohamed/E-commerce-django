from . import views
from django.urls import path


app_name="orders"

urlpatterns = [
    path('create/', views.order_create,name='order_create'),
    path('pay-order/<int:order_id>/', views.order_pay_by_vodafone,name='pay_order'),
    path('payment_success/<int:order_id>/', views.payment_success,name='payment_success'),

]