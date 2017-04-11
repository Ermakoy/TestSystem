from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from  rest_framework import generics
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
    return render_to_response('testsystem/subject.html', args)

def get_test(request,subs, subject, num):
    args = choose(subject)
    args['queryset'] = tasks.objects.filter(test_id=num, subject_id=subject.capitalize())
    return render_to_response('testsystem/test.html', args)

class ListCreateTasks(generics.ListCreateAPIView):
    queryset = tasks.objects.all()
    serializer_class = TasksSerializer





