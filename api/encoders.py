from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from django.db.models.query import QuerySet
from django.urls import reverse

from api.models import Student


class JsonEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, QuerySet):
            return list(obj)
        """ i = 0
         json = serializers.serialize("python", obj, ensure_ascii=False)
         for x in obj:
             teacher_id = json[i]['fields']['teacher']
             student_id = json[i]['pk']
             print(teacher_id)
             json[i]['details'] = ("http://127.0.0.1:8000" + reverse('students') + "/" + str(student_id))
             json[i]['fields']['teacher'] = "http://127.0.0.1:8000" + reverse('teachers') + "/" + str(teacher_id)
             i += 1
         return json"""

        return DjangoJSONEncoder.default(self, obj)


class TeacherSerializer(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, QuerySet):
            for o in obj:
                t_id = str(o['id'])
                if len(o) == 3:
                    o['details'] = "http://127.0.0.1:8000" + reverse('teacher_detail', args=t_id)
                else:
                    students_of = list(Student.objects.filter(teacher=t_id).values('id', 'lastName', 'firstName'))
                    student_list = []
                    for s in students_of:
                        student_list.append({
                            'name': s['firstName'] + " " + s['lastName'],
                            'url': "http://127.0.0.1:8000" + reverse('student_detail', args=str(s['id']))
                        })
                    o['students'] = student_list
            return list(obj)
        return DjangoJSONEncoder.default(self, obj)


class StudentSerializer(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, QuerySet):
            for o in obj:
                t_id = str(o['teacher'])
                o['teacher'] = "http://127.0.0.1:8000" + reverse('teacher_detail', args=t_id)
                if len(o) == 4:
                    t_id = str(o['id'])
                    o['details'] = "http://127.0.0.1:8000" + reverse('student_detail', args=t_id)
            return list(obj)
        return DjangoJSONEncoder.default(self, obj)
