from django.contrib import admin

# Register your models here.
from user.models import Customer, Tasker, Availability, Date

admin.site.register(Customer)
admin.site.register(Tasker)
admin.site.register(Availability)
admin.site.register(Date)