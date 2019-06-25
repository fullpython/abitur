from rest_framework import serializers
from apps.universities.serializers import FacultySerializer
from .models import Subscription

class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = '__all__'

class SubscriptionDetailSerializer(serializers.ModelSerializer):
    faculty = FacultySerializer()
    class Meta:
        model = Subscription
        fields = '__all__'