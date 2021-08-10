from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.urls import reverse
from django.shortcuts import redirect

from .encoders import StudentSerializer, TeacherSerializer
from .models import Teacher, Student


def index(request):
    json = [
        {'Teachers': "http://127.0.0.1:8000"+reverse('teachers')},
        {'Students': "http://127.0.0.1:8000"+reverse('students')},
    ]
    return JsonResponse(json, safe=False)


def show_teachers(request):
    teachers = Teacher.objects.values(
        'id', 'firstName', 'lastName'
    )
    return JsonResponse(teachers, safe=False, encoder=TeacherSerializer)


def teacher_details(request, teacher_id):
    teacher = Teacher.objects.filter(id=teacher_id).values(
        'id', 'firstName', 'lastName', 'email', 'city', 'street', 'house_number', 'zip_code', 'city'
    )

    return JsonResponse(teacher, safe=False, encoder=TeacherSerializer)


def show_students(request):
    students = Student.objects.values(
        'id', 'firstName', 'lastName', 'teacher'
    )
    return JsonResponse(students, safe=False, encoder=StudentSerializer)


def student_details(request, student_id):
    student = Student.objects.filter(id=student_id).values(
        'id', 'firstName', 'lastName', 'email', 'teacher', 'city', 'street', 'house_number', 'zip_code', 'city'
    )
    return JsonResponse(student,  safe=False, encoder=StudentSerializer)
