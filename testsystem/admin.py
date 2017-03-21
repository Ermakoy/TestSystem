from django.contrib import admin
from testsystem.models import tasks_math, tasks_russian, suggestion, subject, fix_test_math, fix_test_russian

class Tasks_mathAdmin (admin.ModelAdmin):

    list_display_links = ( 'id',)
    list_display = ( 'id', 'task_number', 'task', 'id_subject', 'image')

    search_fields = ('task_number',)

class Tasks_russianAdmin (admin.ModelAdmin):

    list_display_links = ( 'id',)
    list_display = ('id', 'task_number', 'task', 'id_subject', 'image')

    search_fields = ('task_number',)

class SuggestionAdmin (admin.ModelAdmin):

    list_display_links = ('id',)
    list_display = ('id', 'task_number', 'task', 'answer', 'id_subject', 'image', 'flag')

    list_filter = ('flag',)
    search_fields = ('task_number',)

class SubjectAdmin (admin.ModelAdmin):
    list_display_links = ('id',)
    list_display = ('id', 'subject')

class Fix_test_mathAdmin(admin.ModelAdmin):

    list_display_links = ('id',)
    list_display = ('id', 'task_1', 'task_2', 'task_3', 'task_4', 'task_5', 'task_6', 'task_7', 'task_8', 'task_9','task_10', 'task_11','task_12' )

    search_fields = ('id',)

class Fix_test_russianAdmin(admin.ModelAdmin):

    list_display_links = ('id',)
    list_display = ('id', 'task_1', 'task_2', 'task_3', 'task_4', 'task_5', 'task_6', 'task_7', 'task_8', 'task_9','task_10', 'task_11','task_12' )

    search_fields = ('id',)

admin.site.register(tasks_math, Tasks_mathAdmin)
admin.site.register(tasks_russian, Tasks_russianAdmin)
admin.site.register(suggestion, SuggestionAdmin)
admin.site.register(subject, SubjectAdmin)
admin.site.register(fix_test_math, Fix_test_mathAdmin)
admin.site.register(fix_test_russian, Fix_test_russianAdmin)