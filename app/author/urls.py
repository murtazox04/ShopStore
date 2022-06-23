from django.urls import path
from app.author import views

app_name = "main"

urlpatterns = [
    path('', views.Register.as_view(), name='register'),
    # path("login/", views.login_request, name="login"),
    # path("logout", views.logout_request, name= "logout"),
]