from rest_framework.decorators import  api_view
from .serializers import SubjectSerializer, StatictestSerializer
from  rest_framework.response import  Response
from testsystem.models import Subject, tasks



@api_view(['GET'])
def subjects(request):
    data = Subject.objects.all().distinct('subject')
    serializer = SubjectSerializer(data, many=True)
    return  Response(serializer.data)

@api_view(['GET'])
def getsubject(request, subj):
    data = Subject.objects.filter(subjecteng=subj)
    serializer = SubjectSerializer(data, many=True)
    return  Response(serializer.data)

@api_view(['GET'])
def static(request):
    id = request.GET.get('id')
    subject = request.GET.get('subj')
    data = tasks.objects.filter(subject_id=subject, test_id=int(id)).order_by('type_task')
    serializer = StatictestSerializer(data, many=True)
    return Response(serializer.data)

