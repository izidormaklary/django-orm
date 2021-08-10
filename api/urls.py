from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/teachers', views.show_teachers, name='teachers'),
    path('api/students', views.show_students, name='students'),
    path('api/teachers/<int:teacher_id>', views.teacher_details, name='teacher_detail'),
    path('api/students/<int:student_id>', views.student_details, name='student_detail'),
    path('student/add', views.student_add, name='student_add')
]
