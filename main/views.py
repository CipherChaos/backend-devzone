from django.shortcuts import render
from users.models import Profile

def home(request):
    profiles = Profile.objects.all()




    context = {"profiles": profiles}
    return render(request, "home.html",context)




# To DO:
# fix home-page profile icons' urls with introspection method

# view :
#  profile = Profile.objects.first()
#     social_fields = {}
#     for field in profile._meta.get_fields():
#         if field.name.startswith('social_'):
#             social_fields[field.name] = getattr(profile, field.name)


# the second solution would be:
# fix foreignkey for each field