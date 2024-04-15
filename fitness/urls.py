from django.urls import path
from .views import *

urlpatterns = [
    path('add-student', add_student, name='add_student'),
    path('add-trainer', add_trainer, name='add_trainer'),
    path('add-monthprice', add_monthlypricing, name='add_monthlypricing'),

    path('trainer-list/', trainer_list, name='trainer_list'),
    path('', student_list, name='student_list'),
    path('bar-list/', bar_list, name='bar_list'),

]
