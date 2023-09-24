from rest_framework import serializers

from .models import Stats


class VacancyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stats
        fields = "__all__"
