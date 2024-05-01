from django.urls import path
from .views import *

urlpatterns = [
    # Add
    path('add-student/', add_student, name='add_student'),
    path('add-trainer/', add_trainer, name='add_trainer'),
    path('add-monthprice/', add_monthlypricing, name='add_monthlypricing'),
    path('add-bar/', add_bar, name='add_bar'),
    path('add-bar-sold/', add_bar_sold, name='add_bar_sold'),

    # List
    path('trainer-list/', trainer_list, name='trainer_list'),
    path('', student_list, name='student_list'),
    path('bar-list/', bar_list, name='bar_list'),
    path('bar-sold-list/', bar_sold_list, name='bar_sold_list'),
    path('daily-student-list/', daily_student_list, name='daily_student_list'),

    # Panel
    path('trainer-panel/', trainer_panel, name='trainer_panel'),
    path('student-panel/', student_panel, name='student_panel'),
    path('bar-panel/', bar_panel, name='bar_panel'),
    path('bar-sold-panel/', bar_sold_panel, name='bar_sold_panel'),
    path('monthlypricing-panel/', monthlypricing_panel, name='monthlypricing_panel'),

    # Delete
    path('delete-trainer/<int:pk>/', delete_trainer, name='delete_trainer'),
    path('delete-student/<int:pk>/', delete_student, name='delete_student'),
    path('delete-bar/<int:pk>/', delete_bar, name='delete_bar'),
    path('delete-bar-sold/<int:pk>/', delete_bar_sold, name='delete_bar_sold'),
    path('delete-monthlypricing/<int:pk>/', delete_monthlypricing, name='delete_monthlypricing'),

    #Update
    path('update-trainer/<int:pk>/', update_trainer, name='update_trainer'),
    path('update-student/<int:pk>/', update_student, name='update_student'),
    path('update-bar/<int:pk>/', update_bar, name='update_bar'),
    path('update-bar-sold/<int:pk>/', update_bar_sold, name='update_bar_sold'),
    path('update-monthlypricing/<int:pk>/', update_monthlypricing, name='update_monthlypricing'),

    # Account
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),

    path('renew-student/<int:student_id>/', renew_student, name='renew_student'),
]