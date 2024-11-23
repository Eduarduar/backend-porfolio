from django.contrib import admin
from django.urls import path, include
from .views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("", include("about.urls")),
    path("", include("projects.urls")),
    path("", include("social.urls")),
    path("", include("tools.urls")),
    path("", include("projectsTools.urls")),
]
