from django.contrib import admin

# Register your models here.
from user.models import Customer

admin.site.register(Customer)
