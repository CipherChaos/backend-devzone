from django.shortcuts import render
from users.models import Profile
from projects.utils import search_project
from django.shortcuts import redirect


def home(request):
    profiles = Profile.objects.all()

    context = {"profiles": profiles}
    return render(request, "home.html",context)