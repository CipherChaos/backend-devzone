from django.conf import settings
from django.db.models.signals import post_save, post_delete
from .models import Profile
from django.contrib.auth.models import User

from django.core.mail import send_mail
from django.conf import settings


def create_profile(sender, instance, created, **kwargs):

    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            user_name=user.username,
            email=user.email,
            name=user.first_name,
        )

        subject = f"Hello {[profile.name]}, Welcome to Devzone!"
        message = "We're glad you are here!"

        try:
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [profile.email],
                fail_silently=False,

            )
        except:
            print("Email failed to send!")

def update_profile(sender, instance, created, **kwargs):

    profile = instance
    user = profile.user

    if not created:
        user.first_name = profile.name
        user.username = profile.user_name
        user.email = profile.email
        user.save()


def delete_profile(sender, instance, **kwargs):

    user = instance.user
    user.delete()


post_save.connect(create_profile, sender=User)
post_save.connect(update_profile, sender=Profile)
post_delete.connect(delete_profile, sender=Profile)
