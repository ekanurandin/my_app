from django.contrib import admin
from .models import Beranda, Menu 
# Register your models here.

class BerandaAdmin(admin.ModelAdmin):
    list_display = ("nama", "keterangan",)

class MenuAdmin(admin.ModelAdmin):
    list_display = ("nama", "keterangan",)

admin.site.register(Beranda, BerandaAdmin)
admin.site.register(Menu, MenuAdmin)