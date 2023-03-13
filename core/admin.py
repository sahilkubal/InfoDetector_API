from django.contrib import admin
from . models import InfoModel

# Register your models here.
class InfoAdminModel(admin.ModelAdmin):
    list_display = ["image_name","objects_detected","timestamp"]

admin.site.register(InfoModel, InfoAdminModel)
