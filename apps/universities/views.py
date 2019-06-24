from django.shortcuts import render
from rest_framework import viewsets
from .models import (
    University,
    Faculty
)

from .serializers import (
    UniversitySerializer,
    FacultySerializer,
    UniversityDetailSerializer
)
class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            serializer_class = UniversityDetailSerializer
        else:
            serializer_class = UniversitySerializer
        return serializer_class

class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer

    