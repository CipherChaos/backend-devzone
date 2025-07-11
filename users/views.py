from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import  UserCreationForm
from django.contrib import messages
from .models import Profile
from users.forms import CustomUserCreationForm

def logout_user(request):
    logout(request)
    messages.info(request, "User was logged out")
    return redirect("login")


def login_user(request):

    page = "login"

    if request.user.is_authenticated:
        return redirect("profiles")

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "You successfully logged in")
                return redirect('profiles')
            else:
                messages.error(request, "Username OR password is incorrect !")
        except:
            messages.error(request, "Username does not exist !")


    context = {"page":page}
    return render(request, "users/login_register.html", context)


def register_user(request):
    page = "register"
    form =  CustomUserCreationForm()

    if request.method == "POST":
        form =  CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, "User account was created!")

    context = {"page": page, "form":form}
    return render(request, "users/login_register.html", context)

def profiles(request):
    users_profiles = Profile.objects.all()
    context = {"profiles": users_profiles}
    return render(request, "users/profile.html", context)


def user_profile(request, slug):
    profile = Profile.objects.get(slug=slug)
    top_skills = profile.skill_set.exclude(description__exact="")
    other_skills = profile.skill_set.filter(description="")

    context = {"profile": profile, "top_skills": top_skills,
               "other_skills": other_skills}
    return render(request, "users/user-profile.html", context)
