from django.contrib import admin
from dongia_app.models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ("name",)
class DongAdmin(admin.ModelAdmin):
    list_display = ("name","amount","donger","dong","dongia_list")
class DongRecordAdmin(admin.ModelAdmin):
    list_display = ("from_user","to_user","amount","for_dong","paid")

admin.site.register(User,UserAdmin)
admin.site.register(Dong,DongAdmin)
admin.site.register(DongRecord,DongRecordAdmin)
