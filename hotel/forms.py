from django import forms
"""from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User"""
from .models import Reservation
from django.contrib.admin import widgets      


"""class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=30, required=True)
    surname = forms.CharField(max_length=30, required=True)
    phone = forms.CharField(max_length=9, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'name', 'surname', 'phone', 'email', 'password1', 'password2', )
"""
class Booking(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = ('name', 'surname', 'phone', 'email', 'roomType', 'bookIn', 'bookOut',)
        widgets = {
        	'bookIn': forms.DateInput(attrs={'class': 'datepicker'}),
        	'bookOut': forms.DateInput(attrs={'class': 'datepicker'})
        	}