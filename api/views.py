from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from random import sample
from testsystem.models import Subject, tasks, temp_test
from .serializers import SubjectSerializer, TestSerializer, SolveSerializer


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

    p = temp_test(tasks="&".join([str(i) for i in id]), subject=subject)
    p.save()
    data = tasks.objects.filter(id__in=id).order_by('type_task')
    serializer = TestSerializer(data, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def temp(request):

    subject = request.GET.get('subj')
    id = int(request.GET.get('id'))
    id = temp_test.objects.filter(id=id, subject=subject)
    id = [int(i) for i in id[0].tasks.split('&')]
    data = tasks.objects.filter(id__in=id).order_by('type_task')
    serializer = TestSerializer(data, many=True)
    return Response(serializer.data)


"""
@api_view(['GET'])
def task(request):
    id = int(request.GET.get('id'))
"""

@api_view(['GET'])
def answer(request):

    ans = request.GET.getlist('ans')
    id = [int(i) for i in request.GET.getlist('id')]
    subject = request.GET.get('subj')
    TF = [0]*len(ans)
    resp = []
    data = tasks.objects.filter(id__in = id, subject_id = subject).order_by('type_task')

    for i in range(len(ans)):
        if data[i].answer == ans[i]:
            TF[i] = True
        else: TF[i] = False
    for i in range(len(TF)):
        dictin = {}
        dictin['answ'] = TF[i]
        dictin['type_task'] = data[i].type_task
        dictin['id'] = data[i].id
        resp.append(dictin)

    return Response(resp)

@api_view(['GET'])
def solve(request):
    id = request.GET.getlist('id')
    data = tasks.objects.filter(id__in = id)
    serializer = SolveSerializer(data, many=True)
    return Response(serializer.data)