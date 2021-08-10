from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teachers', views.show_teachers, name='teachers'),
    path('students', views.show_students, name='students'),
    path('teachers/<int:teacher_id>', views.teacher_details, name='teacher_detail'),
    path('students/<int:student_id>', views.student_details, name='student_detail'),
]
