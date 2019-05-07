# -*- coding: utf-8 -*-
# Data serializers for API

from arch_api.models import file_data
from rest_framework import serializers

class FileListSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = file_data
		fields = ('f_name', 'f_path', 'f_create', 'f_modify', 'f_size')

class ArchiveListSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = file_data
		fields = ('f_name', 'f_path', 'f_create', 'f_modify', 'f_size')


