from django import forms
from .models import Student, Teacher, User


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['userName','password']