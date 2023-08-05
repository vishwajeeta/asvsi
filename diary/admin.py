from django.contrib import admin
from .models import Notedata
# Register your models here.
class tableAdmin(admin.ModelAdmin):
    list_display= ['dates']
# Register your models here.
admin.site.register(Notedata,tableAdmin)


