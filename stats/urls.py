from django.urls import path, include
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('api/v1/statistic', views.StatsListView.as_view())
]
