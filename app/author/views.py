from django.shortcuts import render, redirect
from app.author.forms import RegistrationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from rest_framework import generics


# Create your views here.

# def register_request(request):
#     if request.method == "POST":
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.success(request, "Registration successful." )
#             # return redirect("main:index")
#         messages.error(request, "Unsuccessful registration. Invalid information.")
#     form = RegistrationForm()
#     return render (request=request, template_name="register.html", context={"register_form":form})
class Register(generics.CreateAPIView):
    template_name = 'register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('app.author')

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                # return redirect("main:index")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form":form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect("main:index")
