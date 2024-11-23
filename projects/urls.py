from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import ProjectsViewSet

router = DefaultRouter()
router.register(r"projects", ProjectsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
