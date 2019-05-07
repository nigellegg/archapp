# -*- coding: utf-8 -*-
# URLs

from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from arch_api import views

router = routers.DefaultRouter()
router.register(r'files', views.FileListViewSet)
router.register(r'archive', views.ArchiveListViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)) 
]
