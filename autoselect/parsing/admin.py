from django.contrib import admin
from .models import Sensor
from .models import Analog
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export import fields
from import_export.widgets import ForeignKeyWidget

# Register your models here.

#class SensorAdmin(admin.ModelAdmin):
#    list_display = ('pk', 'marking',)
#    search_fields = ('marking',)
#    empty_value_display = '-пусто-'

class SensorResource(resources.ModelResource):

    class Meta:
        model = Sensor

class SensorAdmin(ImportExportModelAdmin):
    resource_class = SensorResource
    list_display = ('pk', 'marking',)
    search_fields = ('marking',)
    empty_value_display = '-пусто-'

admin.site.register(Sensor, SensorAdmin)
admin.site.register(Analog, SensorAdmin)

