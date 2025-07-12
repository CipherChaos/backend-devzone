from django.conf.global_settings import LOGIN_REDIRECT_URL
from django.shortcuts import render, redirect
from django.template.defaultfilters import title
from django.contrib.auth.decorators import login_required

from projects.models import Project
from projects.forms import ProjectForm


def products(request):
    page = "products"
    count = 20
    context = {"page": page, "products_count": count}
    return render(request, "projects/products.html", context)


def registration(request):
    age = 19
    context = {"age": age}
    return render(request, "projects/registration.html", context)


def single_project(request, slug):
    project = Project.objects.get(slug=slug)
    context = {"project": project}
    return render(request, "projects/single-project.html", context)


def home(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "projects/home.html", context)

@login_required(login_url="login")
def create_project(request):
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "projects/form.html", context)

@login_required(login_url="login")
def update_form(request, slug):
    project = Project.objects.get(slug=slug)
    form = ProjectForm(instance=project)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "projects/form.html", context)

@login_required(login_url="login")
def delete_project(request, slug):
    project = Project.objects.get(slug=slug)
    form = project
    if request.method == "POST":
        form.delete()
        return redirect("home")

    context = {"object": form}
    return render(request, "projects/delete.html", context)
