from .models import  tasks
from rest_framework import serializers

class TasksSerializer (serializers.ModelSerializer):
    class Meta:
        model = tasks
        fields = ('id', 'subject_id','test_id', 'type_task', 'answer', 'flag', 'task')