from django.urls import path
from django.conf.urls import url, include
# 'abiturs' GET all abiturs
# 'abiturs/34'
# 'abiturs/post 
from rest_framework import routers

from .views import AbiturViewSet

router = routers.DefaultRouter()
router.register(r'^abiturs',AbiturViewSet)

urlpatterns = [
    path('',include(router.urls))
]