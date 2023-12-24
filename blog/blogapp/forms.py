from django import forms
from .models import Books
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title','description','cover']
        widgets={'title':forms.TextInput(attrs={'class':'form-control'}),
                 'description':forms.Textarea(attrs={'class':'form-control'}),
                 'cover':forms.FileInput(attrs={'class':'form-control'})}


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username','email','password1','password2',]
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password1':forms.PasswordInput(attrs={'class':'form-control'}),        
            'password2':forms.PasswordInput(attrs={'class':'form-control'}),      
             }
