from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import json

# Create your views here.

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('action:', action)
    print('productIt:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderId, created = OrderId.objects.get_or_create(order=order,product=product)

    if action == 'add':
        orderId.quantity = (OrderId.quantity+1)
    elif action == 'remove':
        orderId.quantity = (OrderId.quantity-1)
    orderId.save()

    if orderId.quantity <= 0:
        orderId.delete()
    return JsonResponse('Item was added!', safe=False)
