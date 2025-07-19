from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProjectSerializer
from projects.models import Project

@api_view(['GET'])
def get_routes(request):
    routes = [
        {'GET': '/api/projects'},
        {'GET': '/api/projects/slug'},
        {'GET': '/api/projects/slug/vote'},

        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'},
    ]

    return Response(routes)

@api_view(['GET'])
def get_projects(request):
    projects = Project.objects.all()
    serializers = ProjectSerializer(projects, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def get_project(request,slug):
    project = Project.objects.get(slug=slug)
    serializers = ProjectSerializer(project, many=False)
    return Response(serializers.data)