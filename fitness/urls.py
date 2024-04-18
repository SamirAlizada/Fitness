from django.urls import path
from .views import *

urlpatterns = [
    # Add
    path('add-student/', add_student, name='add_student'),
    path('add-trainer/', add_trainer, name='add_trainer'),
    path('add-monthprice/', add_monthlypricing, name='add_monthlypricing'),

    # List
    path('trainer-list/', trainer_list, name='trainer_list'),
    path('', student_list, name='student_list'),
    path('bar-list/', bar_list, name='bar_list'),

    # Panel
    path('trainer-panel/', trainer_panel, name='trainer_panel'),
    path('student-panel/', student_panel, name='student_panel'),
    path('bar-panel/', bar_panel, name='bar_panel'),

    # Delete
    path('delete-trainer/', delete_trainer, name='delete_trainer'),
    path('delete-student/', delete_student, name='add_student'),
    path('delete-bar/', delete_bar, name='add_bar'),

    #Update
    path('update-trainer/', update_trainer, name='update_trainer'),
    path('update-student/', update_student, name='update_student'),
    path('update-bar/', update_bar, name='update_bar'),

]
