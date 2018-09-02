from rest_framework import serializers
from .models import *


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ('id', 'title', 'text')


class NameSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameName
        fields = ('id', 'name')


class UpdateLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpdateLog
        fields = ('id', 'text', 'date_added')