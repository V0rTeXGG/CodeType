<<<<<<< HEAD
from rest_framework import serializers

from .models import Stats


class StatsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stats
        fields = "__all__"
=======
from rest_framework import serializers

from .models import Stats


class StatsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stats
        fields = "__all__"
>>>>>>> 7e151183a7b993d84b6d5ac7c71646492fa2abb4
