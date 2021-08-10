from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from django.db.models.query import QuerySet
from django.urls import reverse

from api.models import Student


class TeacherSerializer(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, QuerySet):
            for o in obj:
                t_id = o['id']
                if len(o) == 3:
                    o['details'] = "http://127.0.0.1:8000" + reverse('teacher_detail', args=[t_id])
                else:
                    students_of = list(Student.objects.filter(teacher=t_id).values('id', 'lastName', 'firstName'))
                    student_list = []
                    for s in students_of:

                        s_id = s['id']
                        print(student_list)
                        student_list.append({
                            'name': s['firstName'] + " " + s['lastName'],
                            'url': "http://127.0.0.1:8000" + reverse('student_detail', args=[s_id])
                        })
                    o['students'] = student_list
            return list(obj)
        return DjangoJSONEncoder.default(self, obj)


class StudentSerializer(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, QuerySet):
            for o in obj:
                t_id = o['teacher']
                o['teacher'] = "http://127.0.0.1:8000" + reverse('teacher_detail', args=[t_id])
                if len(o) == 4:
                    s_id = o['id']
                    o['details'] = "http://127.0.0.1:8000" + reverse('student_detail', args=[s_id])
            return list(obj)
        return DjangoJSONEncoder.default(self, obj)
