from django.db import models



class tasks(models.Model):
    type_task = models.IntegerField (verbose_name='Номер задания')
    task = models.TextField(verbose_name='Текст задания')
    answer = models.CharField(max_length=20,
                              verbose_name='Ответ')
    image = models.CharField(blank=True,
                             max_length=100,
                             verbose_name='Картинка к заданию')
    subject_choises = (
        ('Math', 'Математика'),
        ('Russian', 'Русскйи язык'),
    )
    subject_id =  models.CharField(max_length=20,
                                   choices=subject_choises,
                                   default='Math',
                                   verbose_name='Предмет')

    test_id = models.IntegerField(blank=True,
                                  verbose_name='Номер теста')

    date_pub = models.DateField(verbose_name='Дата публикации',
                                auto_now_add=True)
    flag_choices = (
        ('0', 'Не проверено'),
        ('1', 'Проверено'),
    )
    flag = models.CharField(max_length=20,
                            default='1',
                            choices=flag_choices)

class tasks_comments(models.Model):
    id_task = models.ForeignKey(tasks)
    comment = models.TextField(verbose_name='Комментарий')


class temp_test(models.Model):
    id_test = models.IntegerField(verbose_name='Тест')
    tasks = models.TextField(verbose_name='Задания')