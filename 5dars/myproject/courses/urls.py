from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_courses_and_students, name='all_courses_and_students'),
    path('course/<int:course_id>/', views.course_students, name='course_students'),
    path('student/<int:student_id>/', views.student_detail, name='student_detail'),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('courses.urls')),
]
