from rest_framework import serializers
from .models import TODO

class TODOSerializer(serializers.ModelSerializer):
    class Meta:
        model=TODO
        fields=['pk', 'item', 'isComplete']