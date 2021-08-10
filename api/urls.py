from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('api/teachers', views.show_teachers, name='teachers'),
    path('api/students', views.show_students, name='students'),
    path('api/teachers/<int:teacher_id>', views.teacher_details, name='teacher_detail'),
    path('api/students/<int:student_id>', views.student_details, name='student_detail'),
    path('student/add', views.student_add, name='student_add'),
    path('student/edit/<int:student_id>', views.student_edit, name='student_edit'),
    path('teacher/add', views.teacher_add, name='teacher_add'),
    path('teacher/edit/<int:teacher_id>', views.teacher_edit, name='teacher_edit'),
]
