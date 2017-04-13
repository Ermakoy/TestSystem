from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render_to_response
from django.db.models import Max


from .models import tasks, Subject
from .serializers import TasksSerializer, TestStaticAnswer



def subject(request, subject_t):
    args = {}
    args['nameoftasks'] = Subject.objects.filter(subjecteng=subject_t)
    args['subjecteng'] = subject_t;
    # Вывод максимального номера статического теста и запись его в args в качестве списка от 1 до n
    args['xrange'] = [
        str(i) for i in range(1, tasks.objects.filter(subject_id=subject_t).aggregate(Max('test_id'))['test_id__max']+1)]
    return render_to_response('testsystem/subject.html', args)

def get_static_test(request, subject_t, num):
    args = {}
    args['nameoftasks'] = Subject.objects.filter(subjecteng=subject_t)
    args['queryset'] = tasks.objects.filter(test_id=num, subject_id=subject_t).order_by('type_task')
    args['subject'] = args['nameoftasks'][0].subject.upper()
    return render_to_response('testsystem/test.html', args)

# Задел под создание и выдачи темп тест
def get_new_temp_test(request, subject_t):
    args = {}

# Задел на json ответ
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





