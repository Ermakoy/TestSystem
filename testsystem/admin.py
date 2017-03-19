from django.contrib import admin
from testsystem.models import tasks

class TaskAdmin (admin.ModelAdmin):

    list_display_links = ( 'id', 'task_number', 'task', 'answer', 'subject', 'image', 'id_test')
    list_display = ( 'id', 'task_number', 'task', 'answer', 'subject', 'image', 'id_test')
    list_filter =  ('subject',)
    search_fields = ('task_number',)


admin.site.register(tasks, TaskAdmin)