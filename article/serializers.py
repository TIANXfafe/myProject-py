from .models import Classify
from rest_framework import serializers


class ClassifySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Classify
        fields = ('id', 'parent_id', 'name', 'creator', 'createdAt', 'status')