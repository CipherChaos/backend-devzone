from django.urls import path

from . import views

urlpatterns = [
    path("profiles/", views.profiles, name="profiles"),
    path("profile/<slug:slug>", views.user_profile, name="user-profile")
]