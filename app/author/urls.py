from django.urls import path
from app.author import views

urlpatterns = [
    path('', views.register_request, name='register'),
    path("login/", views.login_request, name="login")
]