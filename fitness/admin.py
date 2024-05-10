from django.contrib import admin
from .models import MonthlyPricing, Trainer, Student, Bar, BarSold, DailyPricing

admin.site.register(MonthlyPricing)
admin.site.register(Trainer)
admin.site.register(Student)
admin.site.register(Bar)
admin.site.register(BarSold)
admin.site.register(DailyPricing)