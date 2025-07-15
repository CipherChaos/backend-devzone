from django.urls import path
from . import views

urlpatterns = [

    path('', views.projects, name="projects"),
    path('project/<slug:slug>/', views.single_project, name="single-project"),
    path('create-project/', views.create_project, name="create-project"),
    path('update-project/<slug:slug>/', views.update_project,
         name="update-project"),
    path('delete-project/<slug:slug>/', views.delete_project,
         name="delete-project")
]
