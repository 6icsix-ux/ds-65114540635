from django.urls import path
from .views import course_list, edit_course, add_course

urlpatterns = [
    path('', course_list, name='course_list'),
    path('edit/<str:course_code>/', edit_course, name='edit_course'),
    path('add/', add_course, name='add_course'),  # ✅ เส้นทางสำหรับเพิ่มรายวิชา
]
