from django.contrib import admin

# Register your models here.
from service.models import Task, TaskModel, Category, Order

admin.site.register(Task)
admin.site.register(TaskModel)
admin.site.register(Category)
admin.site.register(Order)