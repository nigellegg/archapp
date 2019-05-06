from arch_api.models import file_data
from rest_framework import viewsets
from arch_api.serializers import FileListSerializer, ArchiveListSerializer

class FileListViewSet(viewsets.ModelViewSet):
	queryset = file_data.objects.get(f_archive=False)
	serializer_class = FileListSerializer

class ArchiveListViewSet(viewsets.ModelViewSet):
	queryset = file_data.objects.get(f_archive=True)
	serializer_class = ArchiveListSerializer


