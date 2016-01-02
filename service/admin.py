from django.contrib import admin

# Register your models here.
from service.models import Skill, TaskModel, Category, Order

admin.site.register(Skill)
admin.site.register(TaskModel)
admin.site.register(Category)
admin.site.register(Order)