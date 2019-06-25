from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from .models import Subscription
from .serializers import (
    SubscriptionSerializer,
    SubscriptionDetailSerializer
)

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    pagination_class = LimitOffsetPagination

    def get_serializer_class(self):
        serializer_class = SubscriptionSerializer

        if self.action == 'retrieve':
            serializer_class = SubscriptionDetailSerializer
        
        return serializer_class