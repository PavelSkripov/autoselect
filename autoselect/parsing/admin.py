from django.contrib import admin
from .models import Sensor
from .models import Analog
# Register your models here.

class SensorAdmin(admin.ModelAdmin):
    list_display = ('pk', 'marking',)
    search_fields = ('marking',)
    empty_value_display = '-пусто-'

admin.site.register(Sensor, SensorAdmin)