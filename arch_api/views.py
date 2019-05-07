# -*- coding: utf-8 -*-
# Creates rest-framework viewsets for the api

from arch_api.models import file_data
from rest_framework import viewsets
from arch_api.serializers import FileListSerializer, ArchiveListSerializer

class FileListViewSet(viewsets.ModelViewSet):
	if file_data.objects.all().count() > 0:
		queryset = file_data.objects.get(f_archive=False)
	else:
		queryset = file_data.objects.none()
		serializer_class = FileListSerializer

class ArchiveListViewSet(viewsets.ModelViewSet):
	if file_data.objects.all().count() > 0:
		queryset = file_data.objects.get(f_archive=True)
	else: 
		queryset = file_data.objects.none()
		serializer_class = ArchiveListSerializer


