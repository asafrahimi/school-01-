from django.contrib import admin
from .models import Student, StudentGrade
from .models import Teacher, TeacherField
from .models import Field

#admin.site.register([Id])
admin.site.register(Student)
admin.site.register(StudentGrade)
admin.site.register(Teacher)
admin.site.register(TeacherField)
admin.site.register(Field)
# Register your models here.
