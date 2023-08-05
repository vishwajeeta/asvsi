from django.contrib import admin
from .models import web_app

class web_appAdmin(admin.ModelAdmin):
    list_display= ('App_Name','img','URL')
# Register your models here.
admin.site.register(web_app,web_appAdmin)
admin.site.site_header = 'vishwabhai management system'