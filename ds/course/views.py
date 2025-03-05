from django.shortcuts import render, get_object_or_404, redirect
from .models import Course
from .forms import *
import json

# แสดงรายการวิชา
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course/course_list.html', {'courses': courses})

# แก้ไขข้อมูลรายวิชา
def edit_course(request, course_code):
    course = get_object_or_404(Course, code=course_code)
    
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')  # กลับไปหน้ารายการวิชา
    else:
        form = CourseForm(instance=course)

    return render(request, 'course/edit_course.html', {'form': form, 'course': course})

# ฟังก์ชันสำหรับเพิ่มรายวิชา
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')  # กลับไปที่หน้ารายการวิชา
    else:
        form = CourseForm()
    
    return render(request, 'course/add_course.html', {'form': form})

