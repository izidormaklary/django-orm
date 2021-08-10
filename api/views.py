from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.urls import reverse
from django.template import loader
from django.shortcuts import redirect, render, get_object_or_404

from .encoders import StudentSerializer, TeacherSerializer
from .forms import StudentForm, TeacherForm, RegistrationForm, LoginForm
from .models import Teacher, Student


def index(request):
    json = [
        {'Teachers': "http://127.0.0.1:8000" + reverse('teachers')},
        {'Students': "http://127.0.0.1:8000" + reverse('students')},
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
    return JsonResponse(student, safe=False, encoder=StudentSerializer)


def student_add(request):
    form = StudentForm(request.POST or None)

    if form.is_valid():
        s_model = form.save()
        id = s_model.pk
        return redirect('student_detail', student_id=id)

    template = loader.get_template('student/addstudent.html')
    return HttpResponse(template.render({'form': form}, request))


def student_edit(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        s_model = form.save()
        id = s_model.pk
        return redirect('student_detail', student_id=id)

    template = loader.get_template('student/editstudent.html')
    return HttpResponse(template.render({'form': form, 'student': student}, request))


def teacher_add(request):
    form = TeacherForm(request.POST or None)

    if form.is_valid():
        t_model = form.save()
        id = t_model.pk
        return redirect('teacher_detail', teacher_id=id)

    template = loader.get_template('teacher/addteacher.html')
    return HttpResponse(template.render({'form': form}, request))


def teacher_edit(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    form = TeacherForm(request.POST or None, instance=teacher)

    if form.is_valid():
        t_model = form.save()
        id = t_model.pk
        return redirect('teacher_detail', teacher_id=id)

    template = loader.get_template('teacher/editteacher.html')
    return HttpResponse(template.render({'form': form, 'teacher': teacher}, request))


def login(request):
    form = LoginForm(request.POST or None)
    template = loader.get_template('user/login.html')
    return HttpResponse(template.render({'form': form}), request)


def register(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()
        redirect('index')
    template = loader.get_template('user/register.html')
    return HttpResponse(template.render({'form': form}), request)