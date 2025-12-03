from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("users:profile")
    else:
        form = RegisterForm()

    return render(request, "users/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("users:profile")  # stworzymy za chwilę
        else:
            messages.error(request, "Nieprawidłowy login lub hasło.")

    return render(request, "users/login.html")


@login_required
def profile_view(request):
    return render(request, "users/profile.html")


def logout_view(request):
    logout(request)
    return redirect("users:login")
