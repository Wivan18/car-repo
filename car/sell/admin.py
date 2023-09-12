from django.contrib import admin

from .models import car, category


admin.site.register(category)
admin.site.register(car)
