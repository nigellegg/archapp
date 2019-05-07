# -*- coding: utf-8 -*-
# Model for file meta data.  

from django.db import models

class file_data(models.Model):
	f_name = models.CharField(max_length=50)
	f_path = models.CharField(max_length=50)
	f_create = models.CharField(max_length=25)
	f_modify = models.CharField(max_length=25)
	f_size = models.IntegerField()
	f_archive = models.BooleanField(default=False)


