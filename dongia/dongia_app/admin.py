from django.contrib import admin
from dongia_app.models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ("name",)

admin.site.register(User,UserAdmin)
