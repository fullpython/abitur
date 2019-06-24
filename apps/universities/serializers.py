from rest_framework import serializers
from .models import (
    University,
    Faculty
)


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ['id','university','name','code']


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ['id','name']

class UniversityDetailSerializer(serializers.ModelSerializer):
    faculties_of_university = FacultySerializer(many=True)
    class Meta:
        model = University
        fields = '__all__'

