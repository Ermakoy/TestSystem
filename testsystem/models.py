from django.db import models


class tasks(models.Model):

    task_number = models.IntegerField ()
    task = models.CharField ( max_length= 500 )
    answer = models.CharField ( max_length=20 )
    subject = models.CharField ( max_length= 20 )
    id_test = models.IntegerField ( default= -1)
    image = models.CharField ( max_length= 500, default='NULL' ) # link on picture


class comment_task (models.Model):

    id_task = models.ForeignKey ( tasks )
    comment = models.CharField (max_length= 500 )


class temp_test (models.Model):
    id_test = models.IntegerField()
    id_task = models.ForeignKey( tasks )


class suggestion ( models.Model ):
    task_number = models.IntegerField ( default=-1 )
    task = models.CharField ( max_length= 1000 )
    answer = models.CharField ( max_length=20 )
    subject = models.CharField ( max_length= 20 )
    comment = models.CharField (max_length= 500 )
    image = models.CharField( max_length=500 )  # link on picture
    flag = models.IntegerField ( default= 0 ) # 0 - not seemed; -1 - denied; 1 - accept
