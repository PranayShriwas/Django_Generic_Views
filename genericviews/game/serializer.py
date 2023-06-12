from rest_framework import serializers
from .models import Cloths


class clothserializer(serializers.ModelSerializer):
    class Meta:
        model = Cloths
        fields = '__all__'
