from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	# return HttpResponse('testsystem/index.html')
	return render(request, 'testsystem/index.html')

def subject(request):
    return HttpResponse('testsystem/subjects.html')

def test(request):
    return HttpResponse('testsystem/test.html')






