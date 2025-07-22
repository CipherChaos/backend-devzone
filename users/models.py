from tkinter.constants import CASCADE
from django.contrib.auth.models import User
from django.utils.text import slugify
import uuid

from django.db import models


class Profile(models.Model):
    DEFAULT_PROFILE_IMAGE_PATH = "profiles/default-user-icon.jpeg"

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,
                                blank=True)
    user_name = models.CharField(max_length=50, editable=True, unique=True,
                                 null=False, blank=False)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    headline = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True,
                                      upload_to="profiles/",
                                      default=DEFAULT_PROFILE_IMAGE_PATH)

    social_github = models.CharField(max_length=200, null=True, blank=True)
    social_linkedin = models.CharField(max_length=200, null=True, blank=True)
    social_x = models.CharField(max_length=200, null=True, blank=True)
    social_telegram = models.CharField(max_length=200, null=True, blank=True)
    social_website = models.CharField(max_length=200, null=True, blank=True)
    social_youtube = models.CharField(max_length=200, null=True, blank=True)

    slug = models.SlugField(default='', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,
                          editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user_name)
        super(Profile, self).save(*args, **kwargs)

        if self.slug is None:
            self.slug = slugify(self.user_name)
            self.save()

    @property
    def import_url(self):
        try:
            url = self.profile_image.url
        except:
            url = ''
        return url

    def set_image_to_default(self):
        if self.profile_image and self.profile_image.name != self.DEFAULT_PROFILE_IMAGE_PATH:
            self.profile_image.delete(save=False)

        self.profile_image = self.DEFAULT_PROFILE_IMAGE_PATH
        self.save()

    def __str__(self):
        return str(self.user.username)

    class Meta:
        ordering = ["created"]


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


class Message(models.Model):
    sender = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True)

    recipient = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="messages")

    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)

    subject = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField()

    is_read = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.subject
    class Meta:
        ordering = ["is_read","-created"]