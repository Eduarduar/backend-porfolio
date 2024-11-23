from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from django.utils.translation import gettext_lazy as _
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import ProjectSerializer
from .models import Project


class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
