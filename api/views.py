from rest_framework.decorators import  api_view
from .serializers import TasksSerializer
from  rest_framework.response import  Response
from testsystem.models import Subject



@api_view(['GET'])
def getsubjects(request):
    subjects = Subject.objects.all().distinct('subject')
    serializer = TasksSerializer(subjects, many=True)
    return  Response(serializer.data)