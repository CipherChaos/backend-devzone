from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile, Skill
from users.forms import CustomUserCreationForm, ProfileForm, SkillForm, SendMessage
from .utils import search_profiles, profile_paginator


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
                return redirect(request.GET[
                                    'next'] if 'next' in request.GET else 'account')
            else:
                messages.error(request, "Username OR password is incorrect !")
        except:
            messages.error(request, "Username does not exist !")

    context = {"page": page}
    return render(request, "users/login-register.html", context)


def register_user(request):
    page = "register"
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, "User account was created!")
            return redirect('profiles')

    context = {"page": page, "form": form}
    return render(request, "users/login-register.html", context)


def profiles(request):
    users_profiles, search_query = search_profiles(request)
    custom_range, users_profiles = profile_paginator(request, users_profiles,
                                                     6)

    context = {"profiles": users_profiles, "search_query": search_query,
               "custom_range": custom_range}
    return render(request, "users/profile.html", context)


def user_profile(request, slug):
    profile = Profile.objects.get(slug=slug)
    top_skills = profile.skill_set.exclude(description__exact="")
    other_skills = profile.skill_set.filter(description="")

    context = {"profile": profile, "top_skills": top_skills,
               "other_skills": other_skills}
    return render(request, "users/user-profile.html", context)


@login_required(login_url='login')
def user_account(request):
    profile = request.user.profile
    skills = profile.skill_set.all()
    projects = profile.project_set.all()

    context = {"profile": profile, "skills": skills, "projects": projects}
    return render(request, "users/account.html", context)


@login_required(login_url='login')
def edit_account(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Changes has successfully submitted!")
            return redirect("account")

    context = {"form": form}
    return render(request, "users/profile-form.html", context)


@login_required(login_url='login')
def create_skill(request):
    profile = request.user.profile
    form = SkillForm()

    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, "New skill was added successfully")
            return redirect("account")

    context = {"form": form}
    return render(request, "users/skill-form.html", context)


@login_required(login_url='login')
def update_skill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)

    if request.method == "POST":
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.info(request, "skill was updated")
            return redirect("account")

    context = {"form": form}
    return render(request, "users/skill-form.html", context)


@login_required(login_url='login')
def delete_skill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    if request.method == "POST":
        skill.delete()
        messages.error(request, "skill was deleted! ")
        return redirect("account")
    context = {"object": skill}
    return render(request, "delete.html", context)


@login_required(login_url='login')
def inbox_messages(request):
    profile = request.user.profile
    message_request = profile.messages.all()
    unread_message_count = message_request.filter(is_read=False).count

    context = {"message_request": message_request,
               "unread_message_count": unread_message_count}
    return render(request, "users/inbox.html", context)


@login_required(login_url='login')
def view_message(request, pk):
    profile = request.user.profile
    message = profile.messages.get(id=pk)
    if message.is_read is False:
        message.is_read = True
        message.save()
    context = {"message": message}
    return render(request, "users/message.html", context)


def create_message(request, pk):
    recipient = Profile.objects.get(id=pk)
    form = SendMessage()

    try:
        sender = request.user.profile
    except:
        sender = None

    if request.method == "POST":
        form = SendMessage(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.recipient = recipient

            if sender:
                message.name = sender.name
                message.email = sender.email
            message.save()

            messages.success(request, "your message was successfully sent")
            return redirect("profiles")

    context = {"recipient": recipient, "form":form}
    return render(request, "users/message-form.html", context)
