from django.shortcuts import render
from .models import tasks

def index(request):

    return  render(request, 'testsystem/index.html')

def preview(request):

    return  render(request, 'testsystem/preview.html')

def get_test(request):

    test = tasks.objects.filter (test_id = 1).order_by('type_task')

    return render(request, 'testsystem/test.html', {'test': test})