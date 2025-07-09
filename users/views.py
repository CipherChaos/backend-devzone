from django.shortcuts import render
from .models import Profile


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
