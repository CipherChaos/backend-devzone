from tkinter.constants import CASCADE
from django.contrib.auth.models import User
from django.utils.text import slugify
import uuid

from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,
                                blank=True)
    user_name = models.CharField(max_length=50, editable=True, unique=True,
                                 null=False, blank=False)
    name = models.CharField(max_length=200, default=user_name,null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    headline = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True,
                                      upload_to="profiles/",
                                      default="profiles/default-user-icon.jpeg")

    social_github = models.CharField(max_length=200, null=True, blank=True)
    social_linkedin = models.CharField(max_length=200, null=True, blank=True)
    social_x = models.CharField(max_length=200, null=True, blank=True)
    social_telegram = models.CharField(max_length=200, null=True, blank=True)
    social_website = models.CharField(max_length=200, null=True, blank=True)
    social_youtube = models.CharField(max_length=200, null=True, blank=True)


    slug = models.SlugField(default=user_name, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,
                          editable=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user_name)
            super(Profile, self).save(*args,**kwargs)

    def __str__(self):
        return str(self.user.username)


class Skill(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True,
                              blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,
                          editable=False)

    def __str__(self):
        return str(self.name)
