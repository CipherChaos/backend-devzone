from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_routes),
    path('projects/', views.get_projects),
    path('projects/project/<slug:slug>', views.get_project)

]