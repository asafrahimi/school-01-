from rest_framework import serializers
from .models import Student, StudentGrade
from .models import Teacher, TeacherField
from .models import Field
from rest_framework.renderers import JSONRenderer

class StudentSerializer(serializers.ModelSerializer):

    #snipping = serializers.StringRelatedField(many=True)

    class Meta:
        model = Student
        #fields = ['id', 'name', 'last_name', 'age', 'array_of_fields_student']
        fields = ['i_d', 'first_name', 'last_name']
        #fields = "__all__"

    #def get_snipping(self, obj):
    #    return (obj.id)

class StudentGradeSerializer(serializers.ModelSerializer):
    #snipping = serializers.RelatedField(many=True, read_only=True)

    class Meta:
        model = StudentGrade
        fields = ['i_d', 'name', 'grade', 'student_details']


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = ['i_d', 'first_name', 'last_name']

class TeacherFieldSerializer(serializers.ModelSerializer):

    class Meta:
        model = TeacherField
        fields = ['i_d', 'teacher_field', 'teacher_details']

class FieldSerializer(serializers.ModelSerializer):

    class Meta:
        model = Field
        fields = ['i_d', 'field_name']
