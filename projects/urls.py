from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('products/<str:pk>/', views.products, name="products"),
    path('registration/', views.registration, name="registration"),
    path('project/<slug:slug>/', views.single_project, name="single-project"),
    path('create-project/', views.create_form, name="create-project"),
    path('update-project/<slug:slug>/', views.update_form,
         name="update-project"),
    path('delete-project/<slug:slug>/', views.delete_form,
         name="delete-project")
]
