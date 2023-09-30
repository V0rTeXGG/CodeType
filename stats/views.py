from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
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
