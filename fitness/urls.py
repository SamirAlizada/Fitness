from django.urls import path
from .views import student_register

urlpatterns = [
    path('student/register/', student_register, name='student_register'),
]
