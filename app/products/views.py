from django.shortcuts import render
from app.products.models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.

# def store(request):
#     if request.user.is_authenticated:
#         customer = request.user.customer
#         order, created = Order.objects.get_or_create(customer=customer, complete=False)
#         items = order.orderid_set.all()
#         cartItems = order.get_cart_items
#     else:
#         items = []
#         order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
#         cartItems = order['get_cart_items']

#     products=Product.objects.all()
#     context={'products':products,'cartItems':cartItems}
#     return render(request,'Store/Store.html',context)
class ProductView(ListView):
    model = Product
    template_name = 'blog/index.html'
    context_object_name = 'products'

class ContactView(ListView):
    model = Product
    template_name = 'blog/contact.html'
    context_object_name = 'contacts'


class SingleView(ListView):
    model = Product
    template_name = 'blog/single.html'
    context_object_name = 'single'

    def get_queryset(self):
        return Product.objects.get(id=self.kwargs.get('id'))
    
class ProductListView(ListView):
    model = Product
    template_name = 'blog/products.html'
    context_object_name = 'products'
    success_url = '/'
