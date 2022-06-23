from django import forms
from .models import Customer


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField()

    class Meta:
        model = Customer
        fields = '__all__'