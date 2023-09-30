"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os

from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.views.generic import TemplateView, RedirectView
from django.views.static import serve

favicon_view = RedirectView.as_view(url=os.path.join(settings.STATIC_URL, 'favicon.svg'), permanent=True)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('favicon.svg', favicon_view),
    path('', TemplateView.as_view(template_name='index.html')),
    path('', include('stats.urls')),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.jwt')),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    re_path(r'^dmedia/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': os.path.join(settings.VUE_ROOT, 'media')}),
    re_path(r'^img/(?P<path>.*)$', serve, {'document_root': os.path.join(settings.VUE_ROOT, 'img')}),
    re_path(r'^js/(?P<path>.*)$', serve, {'document_root': os.path.join(settings.VUE_ROOT, 'js')}),
    re_path(r'^css/(?P<path>.*)$', serve, {'document_root': os.path.join(settings.VUE_ROOT, 'css')}),
    re_path(r'^fonts/(?P<path>.*)$', serve, {'document_root': os.path.join(settings.VUE_ROOT, 'fonts')}),
]
