import json
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django import forms
from . import forms, models, parse_sensor
from .models import Analog, Sensor

# Create your views here.

def search(marking):
    url = f'https://sensor-com.ru/search/?query=ВБИ-М08-45Р-1112-З'
    return HttpResponseRedirect(f'analogs/{marking}/')


def index(request):
    template = 'parsing/index.html'
    #form = forms.AddForm()
    if request.method == 'POST':
        form = forms.AddForm(request.POST)
        if form.is_valid():
            marking = form.cleaned_data['marking']
            print(form.cleaned_data)
            marking_exists = marking is not None and Analog.objects.filter(marking=marking).exists()
            if marking_exists == True:
                return HttpResponseRedirect(f'analogs/{marking}/')
            else:
                return search(marking)

            #except:
            #try:
            #    models.Analog.objects.create(**form.cleaned_data)
            #    #return redirect('home')
            #except:
            #    form.add_error(None, 'Ошибка добавления маркировки аналога')
    else:
       form = forms.AddForm()

    return render(request, template, {'form': form})
    

def analogs(request):
    template = 'parsing/analogs_list.html'
    analogs = Analog.objects.all
    context = {
        'list' : list,
        'analogs' : analogs,
    }
    return render(request, template, context)

def not_found(request):
    template = 'parsing/not_found.html'
    return render(request, template)

def analog_detail(request, marking):
    #list = get_object_or_404(Analog, marking=marking)
    data = ''
    jsonDec = json.decoder.JSONDecoder()
    mark_list = []
    mark_list.append(marking)
    if not Analog.objects.filter(marking=marking).exists():
        data = parse_sensor.parse_products(mark_list)
        print(data)
    if data == 'marking_not_found':
        return HttpResponseRedirect('/not_found/')
    template = 'parsing/analogs_detail.html'
    analog = Analog.objects.get(marking=marking)
    if analog.difference:
        difference = jsonDec.decode(analog.difference)
    else:
        difference = None
    if analog.difference1:
        difference1 = jsonDec.decode(analog.difference1)
    else:
        difference1 = None
    if analog.difference2:
        difference2 = jsonDec.decode(analog.difference2)
    else:
        difference2 = None
    if analog.difference3:
        difference3 = jsonDec.decode(analog.difference3)
    else:
        difference3 = None
    if analog.difference4:
        difference4 = jsonDec.decode(analog.difference4)
    else:
        difference4 = None
    
    context = {
        #'list' : list,
        'analog' : analog,
        'marking' : marking,
        'difference' : difference,
        'difference1' : difference1,
        'difference2' : difference2,
        'difference3' : difference3,
        'difference4' : difference4,
    }
    return render(request, template, context)

