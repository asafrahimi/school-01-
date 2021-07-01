from django.conf.urls import include, url
from django.urls import path, include
from django.http import HttpResponse
from django.contrib import admin

from rest_framework.urlpatterns import format_suffix_patterns
from . import views
#from .views import IdList
from .views import StudentsView, StudentView
from .views import StudentsGradesView, StudentGradeView
from .views import TeachersView, TeacherView
from .views import TeachersFieldsView, TeacherFieldView
from .views import FieldsView, FieldView


urlpatterns = [
    #url(r'^$', views.index_student, name='index_student'),
    path('students/', StudentsView),
    path('student/<int:nm>/', StudentView),
    path('studentsgrades/', StudentsGradesView),
    path('studentgrade/<int:nm>/', StudentGradeView),

    path('teachers/', TeachersView),
    path('teacher/<int:nm>/', TeacherView),
    path('teachersfields/', TeachersFieldsView),
    path('teacherfield/<int:nm>/', TeacherFieldView),

    path('fields/', FieldsView),
    path('field/<int:nm>/', FieldView),
]
