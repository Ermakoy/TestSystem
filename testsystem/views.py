from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.shortcuts import render_to_response


from .models import tasks, Subject
from .serializers import TasksSerializer



def subject(request, subject_t):
    args = {}
    args['nameoftasks'] = Subject.objects.filter(subjecteng=subject_t)
    args['subjecteng'] = subject_t;
    args['xrange'] = ['1','2','3','4','5','6']
    return render_to_response('testsystem/subject.html', args)

def get_test(request, subject_t, num):
    args = {}
    args['subject'] = subject_t
    args['nameoftasks'] = Subject.objects.filter(subjecteng=subject_t)
    args['queryset'] = tasks.objects.filter(test_id=num, subject_id=subject_t)
    return render_to_response('testsystem/test.html', args)


@api_view(['GET', 'POST'])
def tasks_list(request):

    if request.method == 'GET':
        task = tasks.objects.all()
        serializer = TasksSerializer(task, many=True)
        return Response (serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TasksSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def tasks_detail(request, pk):

    try:
        task = tasks.objects.get(pk=pk)
    except tasks.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TasksSerializer(task)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TasksSerializer(task, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        task.delete()
        return HttpResponse(status=204)




