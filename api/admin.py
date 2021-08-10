from django.contrib import admin

from .models import Teacher, User, Student

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(User)
