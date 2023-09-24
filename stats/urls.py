from django.urls import path, include
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('statistic/', TemplateView.as_view(template_name='index.html')),
]
