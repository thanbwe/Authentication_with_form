from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        print(username,email,password,confirm_password)

        # Basic validations
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
        else:
            # Create user
            user = User.objects.create(
                username=username,
                email=email,
                password=make_password(password)
            )
            messages.success(request, "Registration successful")
            return redirect("login")  # or home page
    return render(request, 'Auth/register.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome, {username}!")
            return redirect("home")  # redirect to home or dashboard
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "Auth/login.html")

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("login") 

