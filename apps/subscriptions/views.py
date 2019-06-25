from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from .models import Subscription
from .serializers import (
    SubscriptionSerializer,
    SubscriptionDetailSerializer
)

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    pagination_class = LimitOffsetPagination

    @action(detail=False, methods=['get'])
    def show_all_subscribers_counts(self,request):
        count = Subscription.objects.all().count()
        return Response({'result':count})
    
    @action(detail=True,methods=['post'])
    def like(self,request,pk=None):
        subscription = Subscription.objects.get(pk=pk)
        subscription.likes +=1
        subscription.save()
        return Response(SubscriptionSerializer(subscription).data)
    
    
    @action(detail=True,methods=['post'])
    def unlike(self,request,pk=None):
        subscription = Subscription.objects.get(pk=pk)
        if subscription.likes>=1:
            subscription.likes -=1
        subscription.save()
        return Response(SubscriptionSerializer(subscription).data)



    def get_serializer_class(self):
        serializer_class = SubscriptionSerializer

        if self.action == 'retrieve':
            serializer_class = SubscriptionDetailSerializer
        
        return serializer_class