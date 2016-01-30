from django.contrib import admin

from service.models import Skill, Category, Order, OrderBasket

admin.site.register(Skill)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderBasket)
