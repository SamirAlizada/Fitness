from django.urls import path
from .views import *

urlpatterns = [
    # Add
    path('add-student/', add_student, name='add_student'),
    path('add-trainer/', add_trainer, name='add_trainer'),
    path('add-monthprice/', add_monthlypricing, name='add_monthlypricing'),
    path('add-bar/', add_bar, name='add_bar'),

    # List
    path('trainer-list/', trainer_list, name='trainer_list'),
    path('student-list', student_list, name='student_list'),
    path('bar-list/', bar_list, name='bar_list'),
    path('', daily_student_list, name='daily_student_list'),

    # Panel
    path('trainer-panel/', trainer_panel, name='trainer_panel'),
    path('student-panel/', student_panel, name='student_panel'),
    path('bar-panel/', bar_panel, name='bar_panel'),
    path('monthlypricing-panel/', monthlypricing_panel, name='monthlypricing_panel'),

    # Delete
    path('delete-trainer/<int:pk>/', delete_trainer, name='delete_trainer'),
    path('delete-student/<int:pk>/', delete_student, name='delete_student'),
    path('delete-bar/<int:pk>/', delete_bar, name='delete_bar'),
    path('delete-monthlypricing/<int:pk>/', delete_monthlypricing, name='delete_monthlypricing'),

    #Update
    path('update-trainer/<int:pk>/', update_trainer, name='update_trainer'),
    path('update-student/<int:pk>/', update_student, name='update_student'),
    path('update-bar/<int:pk>/', update_bar, name='update_bar'),
    path('update-monthlypricing/<int:pk>/', update_monthlypricing, name='update_monthlypricing'),

    # Account
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
