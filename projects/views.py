from django.conf.global_settings import LOGIN_REDIRECT_URL
from django.shortcuts import render, redirect
from django.template.defaultfilters import title
from django.contrib.auth.decorators import login_required
from .models import Project, Tag
from .forms import ProjectForm
from .utils import search_project, project_paginator


def projects(request):
    projects, search_query = search_project(request)
    custom_range, projects = project_paginator(request, projects, 6)

    context = {"projects": projects, 'search_query':search_query, "custom_range":custom_range}
    return render(request, "projects/projects.html", context)


def single_project(request, slug):
    project = Project.objects.get(slug=slug)
    context = {"project": project}
    return render(request, "projects/single-project.html", context)

@login_required(login_url="login")
def create_project(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect("account")

    context = {"form": form}
    return render(request, "projects/form.html", context)


@login_required(login_url="login")
def update_project(request, slug):
    profile = request.user.profile
    project = profile.project_set.get(slug=slug)
    form = ProjectForm(instance=project)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect("projects")

    context = {"form": form}
    return render(request, "projects/form.html", context)


@login_required(login_url="login")
def delete_project(request, slug):
    profile = request.user.profile
    project = profile.project_set.get(slug=slug)
    form = project
    if request.method == "POST":
        form.delete()
        return redirect("projects")

    context = {"object": form}
    return render(request, "delete.html", context)
