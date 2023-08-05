from django.contrib import admin
from .models import flutter_data,C_data,django_data,web3,solidity

class flutter_appAdmin(admin.ModelAdmin):
    list_display= ['App_Name','img']
# Register your models here.
admin.site.register(flutter_data,flutter_appAdmin)
admin.site.register(C_data,flutter_appAdmin)
admin.site.register(django_data,flutter_appAdmin)
admin.site.register(web3,flutter_appAdmin)
admin.site.register(solidity,flutter_appAdmin)
admin.site.site_header = 'flutter management system'