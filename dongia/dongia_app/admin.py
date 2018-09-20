from django.contrib import admin
from dongia_app.models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ("name",)
class DongAdmin(admin.ModelAdmin):
    list_display = ("name","amount","donger","dong","dongia_list")

admin.site.register(User,UserAdmin)
admin.site.register(Dong,DongAdmin)
