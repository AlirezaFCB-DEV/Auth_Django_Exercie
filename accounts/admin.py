from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as Base_User_Admin
from .models import User
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
# Register your models here.

class User_Creation_Form(forms.ModelForm):
    password1 = forms.CharField(label="password" , widget=forms.PasswordInput)
    password2 = forms.CharField(label="password confirmation" , widget=forms.PasswordInput)
    
    class Meta :
        model = User
        fields = ("email" ,)
    
    def clean_password2(self):
        p1 = self.cleaned_data.get("password1")
        p2 = self.cleaned_data.get("password2")
        if p1 and p2 != p2:
            raise forms.ValidationError("password don't match") 
        return p2
    
    def save(self , commit=True) :
        user = super.save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    
    
class User_Change_Form(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    
    class Meta:
        model = User
        fields = ("email" , "password", "is_active" , "is_staff")
        
@admin.register(User)
class User_Admin(Base_User_Admin):
    form = User_Change_Form
    add_form = User_Creation_Form
    list_display = ("email" , "is_staff" , "is_active")
    list_filter = ("is_staff" , "is_active")
    fieldsets = (
        (None , {"fields" : ("email" , "password")}),
        ("Permissions" , {"fields" : ("is_staff" , "is_active" , "is_superuser")}),
    )
    add_fieldsets = (
        (None , {
                "classes" : ("wide",),
                "fields" : ("email" , "password1" , "password2" , "is_staff" , "is_active")
            }),
    ) 
    
    search_fields = ("email" ,)
    ordering = ("email" ,)