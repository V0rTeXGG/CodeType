from rest_framework import serializers
from .models import Stats


class StatsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stats
        fields = "__all__"
