from django.urls import path
from .views import *

urlpatterns = [
    path('', add_student, name='add_student'),
    path('add-trainer', add_trainer, name='add_trainer'),
    path('add-monthprice', add_monthlypricing, name='add_monthlypricing'),

]
