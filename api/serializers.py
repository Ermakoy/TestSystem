from testsystem.models import tasks, temp_test, tasks_comments, Subject
from rest_framework import serializers


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('subject', 'typeoftask', 'nameoftask', 'subjecteng')