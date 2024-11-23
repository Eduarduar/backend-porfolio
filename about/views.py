from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from django.utils.translation import gettext_lazy as _
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import AboutSerializer
from .models import About


class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
