from django.contrib import admin
from .models import *


class TasksAdmin(admin.ModelAdmin):

    list_display_links = ('id',)

    list_display = (
        'id',        'subject_id',
        'type_task', 'task',
        'answer',    'image',
        'test_id',   'date_pub',
        'flag',)


    list_filter = ('subject_id', 'type_task')


admin.site.register( tasks, TasksAdmin)