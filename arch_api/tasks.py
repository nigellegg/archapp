# -*- coding: utf-8 -*-
# Celery task - collects and saves file meta data
 
from __future__ import absolute_import, unicode_literals
from celery import task
import time

from arch_api.models import file_data
import datetime

CHECKTIME = datetime.timedelta(seconds=600)

format = '%Y-%m-%d %H:%M:%S'

@task
def getdata(task):
    print('in task')
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
        try:
            done = file_data.oobjects.filter(f_name==fname)
            if len(done) == 1:
                done[0].f_modify = mTime
        except:
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
    	


