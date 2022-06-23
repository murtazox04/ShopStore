from django.shortcuts import render
from .models import *
from app.orders.models import *

# Create your views here.

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderid_set.all()
        cartItems = order.get_cart_items
    else:
        items=[]
        order = {'get_cart_total': 0,'get_cart_items': 0,'shipping': False}
        cartItems = order['get_cart_items']
    context={'items': items, 'order': order,'cartItems': cartItems}
    return render(request,'cart.html',context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderid_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0,'shipping': False}
        cartItems = order['get_cart_items']
    context = {'items': items, 'order': order,'cartItems':cartItems}
    return render(request,'checkout.html',context)
