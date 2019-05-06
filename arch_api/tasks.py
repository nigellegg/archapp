# -*- coding: utf-8 -*-


from celery import shared_task
import time

from django.contrib.auth.models import User
from arch_api.models import file_data
import datetime


CHECKTIME = datetime.timedelta(seconds=600)

format = '%Y-%m-%d %H:%M:%S'

@shared_task
def getdata(task):
    next_time = datetime.datetime.now() + CHECKTIME
    again = getdata.apply_async((), eta=next_time)

    chpath = '/home/nigel/re_path'
    files = os.listdir(chpath)
    data = {}
    for file in files:
        rstat = os.stat(path + '/' + file)
        fname = file
        fpath = chpath + '/' + file
        mTime = time(format, time.localtime(rstat[8]))
        cTime = time(format, time.localtime(rstat[9]))
        fsize = rstat[6]
        file = file_data()
        file.f_name = fname
        file.f_path = fpath
        file.f_create = cTime
        file.f_modify = mTime
        file.f_size = fsize
        if datetime.datetime.now() - cTime > 432000:
            file.f_archive = True
        file.save()

    	# write to db - but need to check that there is no 
    	


