from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import ProjectSerializer
from projects.models import Project, Review

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

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_project_vote(request, slug):
    project = Project.objects.get(slug=slug)
    user = request.user.profile
    data = request.data

    review, created = Review.objects.get_or_create(
        owner = user,
        project = project,
    )

    review.value = data["value"]
    review.save()
    project.update_vote_stats()


    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)