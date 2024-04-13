from django.contrib import admin
from .models import MonthlyPricing, Trainer, Student

admin.site.register(MonthlyPricing)
admin.site.register(Trainer)
admin.site.register(Student)