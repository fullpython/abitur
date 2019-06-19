from django.shortcuts import render

from rest_framework import viewsets
from .models import Abitur
from .serializers import AbiturSerializer


class AbiturViewSet(viewsets.ModelViewSet):
    queryset = Abitur.objects.all()
    serializer_class = AbiturSerializer
