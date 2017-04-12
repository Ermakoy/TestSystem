from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.shortcuts import render_to_response

from .models import tasks
from .serializers import TasksSerializer


def choose (name):

    if name == 'math':
        return {'range': ['1. Простейшие текстовые задачи',
                          '2. Чтение графиков и диаграмм',
                          '3. Квадратная решётка, координатная плоскость',
                          '4. Начала теории вероятностей',
                          '5. Простейшие уравнения',
                          '6. Планеметрия: задачи, связанные с углами',
                          '7. Производная и первообразная',
                          '8. Стереометрия',
                          '9. Вычислительные преобразования',
                          '10. Задачи с прикладным содержанием',
                          '11. Текстовые задачи',
                          '12. Наибольшее и наименьшее значение функций'],
                'name': 'МАТЕМАТИКА',
                'subject': 'math'}

    elif name == 'russian':
        return {'range': ['1. Определение главной информации текста',
                          '2. Средства связи предложений в тексте',
                          '3. Определение лексического значения словаь',
                          '4. Постановка ударения',
                          '5. Употребление паронимов',
                          '6. Морфологические нормы (образование форм слова)',
                          '7. Синтаксические нормы. Нормы согласования. Нормы управления',
                          '8. Правописание корней',
                          '9. Правописание приставок',
                          '10. Правописание суффиксов (кроме -Н-/-НН-)',
                          '11. Пра­во­пи­са­ние личных окон­ча­ний глаголов и суф­фик­сов причастий',
                          '12. Правописание НЕ и НИ',
                          '13. Слитное, дефисное, раздельное написание слов',
                          '14. Пра­во­пи­са­ние -Н- и -НН- в суффиксах'],
                'name': 'РУССКИЙ ЯЗЫК',
                'subject': 'russian'}


def subject(request, subject):

    args = choose(subject)
    args['xrange'] = ['1','2','3','4','5']
    return render_to_response('testsystem/subject.html', args)

def get_test(request,subs, subject, num):

    args = choose(subject)
    args['queryset'] = tasks.objects.filter(test_id=num, subject_id=subject.capitalize())
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




