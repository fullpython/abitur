from django.urls import path
from django.conf.urls import url,include

from rest_framework import routers

from .views import SubscriptionViewSet

router = routers.DefaultRouter()
router.register(r'subscriptions',SubscriptionViewSet)

urlpatterns = [
    url(r'^',include(router.urls)),
]