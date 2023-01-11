from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    template = 'parsing/index.html'
    return render(request, template)

def analogs (request):
    return HttpResponse('Список замен')

def analog_detail (request):
    return HttpResponse('Характеристики аналога')