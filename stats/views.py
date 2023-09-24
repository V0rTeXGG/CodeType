from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from django.http import JsonResponse
from .models import Stats


class VacancyListView(APIView):

    def post(self, request):
        vacancy = Stats.objects.create(request.body)
        serializer = VacancyCreateSerializer(vacancy)
        return Response(serializer.data)

    def get(self, request):
        vacancy = Stats.objects.all()
        serializer = VacancyListSerializer(vacancy, many=True)
        return Response(serializer.data)
