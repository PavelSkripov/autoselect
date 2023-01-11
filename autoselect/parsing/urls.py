from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('analogs/', views.analogs),
    path('analogs/<marking>/', views.analog_detail),
]
