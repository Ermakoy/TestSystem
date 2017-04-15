from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render_to_response
from django.http import HttpResponse

from random import sample
from .models import tasks, Subject
from .serializers import TasksSerializer, TestStaticAnswer




def subject(request):
    return HttpResponse('testsystem/subjects.html')






