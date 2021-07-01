from django.shortcuts import get_object_or_404
from django.shortcuts import render
from . import views
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.parsers import JSONParser
from .models import Student, StudentGrade
from .models import Teacher, TeacherField
from .models import Field
from .serializers import StudentSerializer, StudentGradeSerializer
from .serializers import TeacherSerializer, TeacherFieldSerializer
from .serializers import FieldSerializer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json as simplejson
#from django.contrib.auth.models import student
def index_student(request):
    return HttpResponse("<h1>This is the student app homepage</h1>")
'''
class IdList(APIView):

    def get(self, request):
        items = Id.objects.all()
        serializer = IdSerializer(items, many =True)
        return JsonResponse(serializer.data, safe =False)
        #id = Id.objects.all()
        #serializer = IdSerializer(id, many=True)
        #return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        id_data = request.data
        new_id = Id.objects.create(name=id_data["name"], last_name=id_data["last_name"], age=id_data["age"])
        new_id.save()
        serializer = IdSerializer(new_id)
        return Response(serializer.data)

    def delete(request, nm):
        item = Id.objects.get(id = nm)
        item.delete()
        return ("item deleted")
'''

@csrf_exempt
def StudentsView(request):

    if request.method == 'GET':
        students = Student.objects.all()
        items1 = StudentGrade.objects.all()
        serializer = StudentSerializer(students, many =True)
        #items1 = Studentarr.objects.all()
        serializer1 = StudentGradeSerializer(items1, many =True)
        #Item = simplejson.dumps([serializer, serializer1])
        return JsonResponse(serializer.data, safe =False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer =StudentSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status =201)
        return JsonResponse(serializer.errors,status = 400)

@csrf_exempt
def StudentView(request,nm):
    try:
        student = Student.objects.get(i_d = nm)
        #item = Id.objects.filter(Id = 'student_array')
    except Student.DoesNotExist:
        raise Http404('Not found')

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return JsonResponse(serializer.data)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StudentSerializer(student, data = data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status =400)

    if request.method == 'DELETE':
        item.delete()
        #return render(request, 'del_done.html')
        return HttpResponse(status =204)


@csrf_exempt
def StudentsGradesView(request):

    if request.method == 'GET':
        studentsgrades = StudentGrade.objects.all()
        serializer = StudentGradeSerializer(studentsgrades, many =True)
        return JsonResponse(serializer.data, safe =False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer =StudentGradeSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status =201)
        return JsonResponse(serializer.errors,status = 400)

@csrf_exempt
def StudentGradeView(request,nm):
    try:
        studentgrade = StudentGrade.objects.get(i_d = nm)
    except Student.DoesNotExist:
        raise Http404('Not found')

    if request.method == 'GET':
        serializer = StudentGradeSerializer(studentgrade)
        return JsonResponse(serializer.data)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StudentGradeSerializer(studentgrade, data =data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status =400)

    if request.method == 'DELETE':
        studentgrade.delete()
        #return render(request, 'del_done.html')
        return HttpResponse(status =204)
#-------------------End of Student-----------------------------

#---------------------Teachers----------------------------------
@csrf_exempt
def TeachersView(request):

    if request.method == 'GET':
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many =True)
        return JsonResponse(serializer.data, safe =False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer =TeacherSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status =201)
        return JsonResponse(serializer.errors,status = 400)

@csrf_exempt
def TeacherView(request,nm):
    try:
        teacher = Teacher.objects.get(i_d = nm)
    except Teacher.DoesNotExist:
        raise Http404('Not found')

    if request.method == 'GET':
        serializer = TeacherSerializer(teacher)
        return JsonResponse(serializer.data)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TeacherSerializer(teacher, data =data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status =400)

    if request.method == 'DELETE':
        teacher.delete()
        return HttpResponse(status =204)


@csrf_exempt
def TeachersFieldsView(request):

    if request.method == 'GET':
        teacherfield = TeacherField.objects.all()
        serializer = TeacherFieldSerializer(teacherfield, many =True)
        return JsonResponse(serializer.data, safe =False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer =TeacherFieldSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status =201)
        return JsonResponse(serializer.errors,status = 400)

@csrf_exempt
def TeacherFieldView(request,nm):
    try:
        teacherfield = TeacherField.objects.get(i_d = nm)
    except TeacherField.DoesNotExist:
        raise Http404('Not found')

    if request.method == 'GET':
        serializer = TeacherFieldSerializer(teacherfield)
        return JsonResponse(serializer.data)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TeacherFieldSerializer(teacherfield, data =data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status =400)

    if request.method == 'DELETE':
        teacherfield.delete()
        return HttpResponse(status =204)
#-------------------End of Teachers-----------------------------

#---------------------Fields------------------------------------
@csrf_exempt
def FieldsView(request):

    if request.method == 'GET':
        field = Field.objects.all()
        serializer = FieldSerializer(field, many =True)
        return JsonResponse(serializer.data, safe =False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer =FieldSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status =201)
        return JsonResponse(serializer.errors,status = 400)

@csrf_exempt
def FieldView(request,nm):
    try:
        field = Field.objects.get(i_d = nm)
    except Field.DoesNotExist:
        raise Http404('Not found')

    if request.method == 'GET':
        serializer = FieldSerializer(field)
        return JsonResponse(serializer.data)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = FieldSerializer(field, data =data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status =400)

    if request.method == 'DELETE':
        field.delete()
        return HttpResponse(status =204)
#-------------------End of Fields-------------------------------




#class List_student(APIView):

#    authentication_classes = [authentication.TokenAuthentication]
#    permission_classes = [permissions.IsAdminUser]

#    def get(self, request, format=None):
#        students = [student.name for student in Student.objects.all()]
#        return Response(students)


#def index_student(request):
#    return HttpResponse("<h1>This is the student app homepage</h1>")
