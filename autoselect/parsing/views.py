from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django import forms
from . import forms, models
from .models import Analog, Sensor

# Create your views here.

def index(request):
    template = 'parsing/index.html'
    #form = forms.AddForm()
    if request.method == 'POST':
        form = forms.AddForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            #try:
            #    models.Analog.objects.create(**form.cleaned_data)
            #    #return redirect('home')
            #except:
            #    form.add_error(None, 'Ошибка добавления маркировки аналога')
    else:
       form = forms.AddForm()
 
    return render(request, template, {'form': form})
    

def analog (request, slug):
    template = 'parsing/analogs_list.html'
    return render(request, template)

def analogs(request):
    #list = get_object_or_404(Analog)
    template = 'parsing/analogs_list.html'
    #text = 'Здесь будет информация о группах проекта'
    analogs = Analog.objects.all
    context = {
        'list' : list,
        'analogs' : analogs,
    }
    return render(request, template, context)    

def analog_detail (request):
    return HttpResponse('Характеристики аналога')