from django.db import models


# ---------------- Math -------------
class tasks_math(models.Model):

    task_number = models.IntegerField( default = -1)
    id_subject = models.IntegerField( default = -1)


    task = models.CharField ( max_length= 500 )
    image = models.CharField ( max_length= 500, default='NULL' ) # link on picture


class answer_math(models.Model):

    id_task = models.IntegerField (primary_key=True, default=-1)

    answer = models.CharField ( max_length= 20)



class fix_test_math (models.Model):

    task_1 = models.IntegerField( default = -1)
    task_2 = models.IntegerField( default = -1)
    task_3 = models.IntegerField( default = -1)
    task_4 = models.IntegerField( default = -1)
    task_5 = models.IntegerField( default = -1)
    task_6 = models.IntegerField( default = -1)
    task_7 = models.IntegerField( default = -1)
    task_8 = models.IntegerField( default = -1)
    task_9 = models.IntegerField( default = -1)
    task_10 = models.IntegerField( default = -1)
    task_11 = models.IntegerField( default = -1)
    task_12 = models.IntegerField( default = -1)

# ----------------- Russian -------------------

class tasks_russian(models.Model):

    task_number = models.IntegerField( default = -1)
    id_subject = models.IntegerField( default = -1)


    task = models.CharField ( max_length= 500 )
    image = models.CharField ( max_length= 500, default='NULL' ) # link on picture


class answer_russian(models.Model):

    id_task = models.IntegerField (primary_key=True, default=-1)

    answer = models.CharField ( max_length= 20)



class fix_test_russian (models.Model):

    task_1 = models.IntegerField( default = -1)
    task_2 = models.IntegerField( default = -1)
    task_3 = models.IntegerField( default = -1)
    task_4 = models.IntegerField( default = -1)
    task_5 = models.IntegerField( default = -1)
    task_6 = models.IntegerField( default = -1)
    task_7 = models.IntegerField( default = -1)
    task_8 = models.IntegerField( default = -1)
    task_9 = models.IntegerField( default = -1)
    task_10 = models.IntegerField( default = -1)
    task_11 = models.IntegerField( default = -1)
    task_12 = models.IntegerField( default = -1)

# etc ...

#temp
class subject (models.Model):

    subject = models.CharField ( max_length=30)


class temp_test (models.Model):
    
    id_subject = models.IntegerField ( primary_key= True, default=-1)
    
    id_task = models.IntegerField( default = -1)


class suggestion ( models.Model ):
    
    task_number = models.IntegerField ( default=-1 )
    
    task = models.CharField ( max_length= 1000 )
    
    answer = models.CharField ( max_length=20 )
    
    
    id_subject = models.IntegerField( default = -1)
    
    image = models.CharField( max_length=500 )  # link on picture
    
    flag = models.IntegerField ( default= 0 ) # 0 - not seemed; -1 - denied; 1 - accept
