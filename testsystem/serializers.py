from testsystem.models import tasks
from rest_framework import serializers


class TasksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = tasks
        fields = (
        'id',        'subject_id',
        'type_task', 'task',
        'answer',    'image',
        'test_id',   'date_pub',
        'flag')
