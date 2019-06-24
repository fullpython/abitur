from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers

from .views import (
    UniversityViewSet,
    FacultyViewSet
)

router = routers.DefaultRouter()
router.register(r'university',UniversityViewSet)
router.register(r'faculty',FacultyViewSet)

urlpatterns = [
    url(r'^',include(router.urls)),
]