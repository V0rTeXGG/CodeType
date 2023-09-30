<<<<<<< HEAD
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from django.http import JsonResponse
from .models import Stats
from .serializer import StatsListSerializer


class StatsListView(APIView):

    def post(self, request):
        stats = Stats.objects.create(request.body)
        serializer = StatsListSerializer(stats)
        return Response(serializer.data)

    def get(self, request):
        stats = Stats.objects.all()
        serializer = StatsListSerializer(stats, many=True)
        return Response(serializer.data)
=======
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from django.http import JsonResponse
from .models import Stats
from .serializer import StatsListSerializer


class StatsListView(APIView):

    def post(self, request):
        stats = Stats.objects.create(request.body)
        serializer = StatsListSerializer(stats)
        return Response(serializer.data)

    def get(self, request):
        stats = Stats.objects.all()
        serializer = StatsListSerializer(stats, many=True)
        return Response(serializer.data)
>>>>>>> 7e151183a7b993d84b6d5ac7c71646492fa2abb4
