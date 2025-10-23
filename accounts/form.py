from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm

User = get_user_model()

class RegisterFrom(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ("email" , "password1" , "password2")
        
class Login_Form(AuthenticationForm):
    email = forms.EmailField(required=True)
    
    class Meta :
        model = User
        fields = ("email" , "password")
        
        
