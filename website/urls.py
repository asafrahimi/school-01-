
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
#from student.views import IdList

from django.http import HttpResponse
from django.contrib import admin

from rest_framework.urlpatterns import format_suffix_patterns
from student import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('music/', include('music.urls')),
    path('school/', include('student.urls')),
    #path('Id/', views.IdList.as_view()),
    #path('Student/', include('student.urls')),
    #path('StudentGrade/', include('student.urls')),
    #path('StudentArray/', include('student.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
