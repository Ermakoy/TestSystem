from rest_framework.decorators import  api_view
from .serializers import SubjectSerializer, TestSerializer
from  rest_framework.response import  Response
from testsystem.models import Subject, tasks, temp_test
from random import sample
from rest_framework import status


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
    serializer = TestSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def newtemp(request):
    num = [int(i) for i in request.GET.getlist('num')]
    subject = request.GET.get('subj')
    id = []
    for i in range(len(num)):
        data = tasks.objects.filter(subject_id=subject, type_task=i+1)
        try:
            req = sample((0, len(data)-1), num[i])
        except:
            return Response(status=status.HTTP_204_NO_CONTENT)
        for j in req:
            id.append(data[j].id)
    print(id)
    p = temp_test(tasks="&".join([str(i) for i in id]), subject=subject)
    p.save()
    data = tasks.objects.filter(id__in=id)
    serializer = TestSerializer(data, many=True)
    return Response(serializer.data)