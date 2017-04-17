from testsystem.models import tasks, temp_test, tasks_comments, Subject
from rest_framework import serializers


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('subject', 'subjecteng')

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = tasks
        fields = ('id', 'subject_id', 'type_task', 'task', 'image')

class SolveSerializer(serializers.ModelSerializer):
    class Meta:
        model = tasks
        fields = ('id','answer', 'solve', 'solve_image')

