from django import forms
from django.forms import ModelForm
from store.models import Order,customer
from store.models import Document
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class OrderForm(ModelForm):
 required_css_class = 'required'
 class Meta:
    model = Order
    fields = '__all__'

class SignupForm(ModelForm):
   required_css_class = 'required'
   Password = forms.CharField(widget=forms.PasswordInput)
   class Meta:
      model = customer
      fields = '__all__'

class LoginForm(ModelForm):
   required_css_class = 'required'
   Password = forms.CharField(widget=forms.PasswordInput)
   class Meta:
      model = customer
      fields = ('Customer_name', 'Password')

class NewUserForm(AuthenticationForm):
    

    class Meta:
        model = customer
        fields = ('Customer_name', 'Password')



class DocumentForm(forms.ModelForm):
   class Meta:
      model = Document
      fields = ('description', 'document', )