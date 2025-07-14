from .models import Profile, Skill
from django.db.models import Q

def search_profiles(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    skills = Skill.objects.filter(name__iexact=search_query)

    users_profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(headline__icontains=search_query) |
        Q(skill__in=skills)
    )
    return users_profiles, search_query


