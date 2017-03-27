from django.db import models



class tasks (models.Model):

    type_task = models.CharField (  max_length=2,
                                    verbose_name='Номер задания')

    subject_choise = (
        ('None', 'Не выбрано'),
        ('Math', 'Математика'),
        ('Russian', 'Русскйи язык'),
    )

    subject =  models.CharField ( max_length=20,
                                  choices=subject_choise,
                                  default='None',
                                  verbose_name='Предмет')

    task = models.TextField(verbose_name='Текст задания')

    answer = models.CharField ( max_length=20,
                                verbose_name='Ответ')

    image = models.CharField ( max_length=100,
                               verbose_name='Картинка к заданию')

    test_id = models.CharField ( max_length=2,
                                 blank=True,
                                 verbose_name='Номер теста')

    date_pub = models.DateField ( auto_now_add=True )



class tasks_comments (models.Model):

    id_task = models.ForeignKey  (tasks)

    comment = models.TextField ( verbose_name='Комментарий')


class temp_test (models.Model):

    id_test = models.CharField ( verbose_name='Тест',
                                 max_length=5)
    tasks = models.TextField ( verbose_name='Задания')