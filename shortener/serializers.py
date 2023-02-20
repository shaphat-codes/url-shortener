from rest_framework import serializers
from .models import *

class ShortenerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'