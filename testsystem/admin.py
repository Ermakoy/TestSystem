from django.contrib import admin
from .models import tasks, Subject, temp_test


class TasksAdmin(admin.ModelAdmin):

    list_display_links = (
        'id',        'subject_id',
        'type_task', 'task',
        'answer',    'image',
        'solve',     'solve_image',
        'test_id',   'date_pub',
        'flag',)

    list_display = (
        'id',        'subject_id',
        'type_task', 'task',
        'answer',    'image',
        'solve',     'solve_image',
        'test_id',   'date_pub',
        'flag',)


    list_filter = ('subject_id',)

class SubjectAdmin (admin.ModelAdmin):

    list_display_links = ('id',)

    list_display =  (
        'id',
        'typeoftask',
        'nameoftask',
        'subject',
        'subjecteng'
    )
class TempAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'tasks')

admin.site.register( temp_test, TempAdmin)
admin.site.register( tasks, TasksAdmin)
admin.site.register( Subject, SubjectAdmin)