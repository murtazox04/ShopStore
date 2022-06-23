from django.urls import path
from . import views

urlpatterns=[
    # path('',views.store,name='store'),
    path('', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    # path('update_item/',views.updateItem,name='update'),

]