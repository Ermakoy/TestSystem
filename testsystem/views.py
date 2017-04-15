from django.http import HttpResponse






def subject(request):
    return HttpResponse('testsystem/subjects.html')

def test(request):
    return HttpResponse('testsystem/test.html')






