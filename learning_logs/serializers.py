from rest_framework import serializers
from .models import *


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id', 'owner', 'text', 'date_added')


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ('id', 'owner', 'topic', 'title', 'text', 'date_added')
