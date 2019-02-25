from django.contrib import admin

# Register your models here.
from player.models import Order, Name

admin.site.register(Order)
admin.site.register(Name)



