from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .form import RegisterFrom
# Create your views here.


def register_view(req):
    if req.method == "POST":
        form = RegisterFrom(req.POST, req.FILES)
        if form.is_valid():
            user = form.save()
            login(req, user)
            return redirect("accounts:profile")
    else:
        form = RegisterFrom()
        return render(req, "accounts/register.html", {"form": form})

@login_required 
def profile_view(req):
    return render(req , "accounts/profile.html", {"user" , req.user})
