from django.urls import path
from . import views

app_name = 'parsing'

urlpatterns = [
    path('', views.index, name='index'),
    path('analogs/', views.analogs, name='analogs'),
    path('analogs/<marking>/', views.analog_detail, name='analog_detail'),
]
