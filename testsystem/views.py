from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render_to_response


from .models import tasks, Subject
from .serializers import TasksSerializer, TestStaticAnswer



def subject(request, subject_t):
    args = {}
    args['nameoftasks'] = Subject.objects.filter(subjecteng=subject_t)
    args['subjecteng'] = subject_t;
    args['xrange'] = ['1','2','3','4','5','6']
    return render_to_response('testsystem/subject.html', args)

def get_static_test(request, subject_t, num):
    args = {}
    args['subject'] = subject_t
    args['nameoftasks'] = Subject.objects.filter(subjecteng=subject_t)
    args['queryset'] = tasks.objects.filter(test_id=num, subject_id=subject_t)
    return render_to_response('testsystem/test.html', args)

def check_static_test(request, subject_t, num, answer_t):
    queryset = tasks.objects.filter(test_id=num, subject_id=subject_t).order_by('type_task')
    serializer = TestStaticAnswer(tasks, many=True)


@api_view(['GET', 'POST'])
def tasks_list(request):

    if request.method == 'GET':
        task = tasks.objects.all()
        serializer = TasksSerializer(task, many=True)
        return Response (serializer.data)

    elif request.method == 'POST':
        serializer = TasksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, serializer=status.HTTP_400_BAD_REQUEST)





