from django.contrib import admin
from .models import  Task
# Register your models here.

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display=['name','email','password']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display=['task_name','written_by']
