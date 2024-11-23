from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from django.utils.translation import gettext_lazy as _
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import ProjectToolSerializer
from .models import ProjectTool


class ProjectToolViewSet(viewsets.ModelViewSet):
    queryset = ProjectTool.objects.all()
    serializer_class = ProjectToolSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
