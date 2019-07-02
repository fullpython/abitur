
from rest_framework import serializers
from .models import Abitur

class AbiturSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abitur
        fields = '__all__'