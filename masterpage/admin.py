from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .import models
# Register your models here.
class NoticeAdmin(ModelAdmin):
    list_display=["subject","date"]
    search_fields=["subject","date"]
    list_filter=["date"]
admin.site.register(models.Notice,NoticeAdmin)
