from django.http import HttpResponse
from django.shortcuts import render


def index(request):
	return render(request, 'testsystem/index.html')


def subject(request):
    return HttpResponse('testsystem/subjects.html')

def test(request):
    return HttpResponse('testsystem/test.html')






