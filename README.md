# re_archive

Archive app for RHEA test
1.  A small django app. 
2.  Web page for uploading files.  
3.  Uses django celery to poll a directory every 10 minutes for new files. 
4.  File metadata is inserted to a postgres database. 
5.  Files more than 5 days old are moved to another directory, and the records for them in the database are tagged. 
6.  API created using the django REST framework, to allow download of data for current and archived files. 

All created with most uptodatwe versions of libraries.  

Need to filter data at two stages: 
1.  If there is no data in the table, then the apis should return "no data", not an error. 
2.  Need to filter out repeat files from the table - if a file is a repeat, check and update f_modify.  If it has not been modified in five days, then archive flag.  
