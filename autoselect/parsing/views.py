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

def analog_detail(request, marking):
    #list = get_object_or_404(Analog, marking=marking)
    mark_list = []
    mark_list.append(marking)
    data = parse_sensor.parse_products(mark_list)
    print(data)
    template = 'parsing/analogs_detail.html'
    #analog = Analog.objects.get(marking=marking)
    context = {
        #'list' : list,
        #'analog' : analog,
        'data' : data,
        'marking' : marking,
    }
    return render(request, template, context)

