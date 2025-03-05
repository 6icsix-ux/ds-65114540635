from django.contrib import admin
from django.urls import path, include
from course.views import course_list  # นำเข้า course_list

urlpatterns = [
    path('courses/', include('course.urls')),  # URL สำหรับ course
    path('', course_list, name='home'),  # ตั้งค่าให้ URL หลักไปที่หน้า course_list
]
