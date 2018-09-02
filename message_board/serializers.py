from rest_framework import serializers
from .models import *


class MesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageBoard
        fields = ('id', 'name', 'text', 'created_time')