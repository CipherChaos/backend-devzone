from django.shortcuts import render
from users.models import Profile



def home(request):
    profiles = Profile.objects.all()

    context = {"profiles": profiles}
    return render(request, "home.html", context)


def error_404(request, exception=None):
    return render(request, '404.html', status=404)

