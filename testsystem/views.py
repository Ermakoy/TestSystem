from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):

    return  render(request, 'testsystem/index.html')

def preview(request):

    return  render(request, 'testsystem/preview.html')