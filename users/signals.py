from django.db.models.signals import post_save, post_delete
from users.models import User,Profile

def create_profile(sender,instance,created,**kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            user_name = user.username,
            email = user.email,
            name = user.first_name,
        )

def delete_profile(sender,instance,**kwargs):
    user = instance.user
    user.delete()

post_save.connect(create_profile,sender=User)
post_delete.connect(delete_profile,sender=Profile)