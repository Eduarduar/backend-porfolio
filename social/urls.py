from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import SocialViewSet

router = DefaultRouter()
router.register(r"social", SocialViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
