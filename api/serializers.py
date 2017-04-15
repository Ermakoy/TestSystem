from testsystem.models import tasks, temp_test, tasks_comments, Subject
from rest_framework import serializers


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('subject', 'subjecteng')

class StatictestSerializer(serializers.ModelSerializer):
    class Meta:
        model = tasks
        fields = ('id', 'subject_id', 'type_task', 'task', 'image')