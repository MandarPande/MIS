from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Students)
class Student(admin.ModelAdmin):
    list_display = ['name','USN','gender','profile_pic','address','contact','course_id','created_at','updated_at' ]

@admin.register(Staffs)
class Staff(admin.ModelAdmin):
    list_display = ['id','address','created_at','updated_at','contact' ]

@admin.register(Courses)
class Course(admin.ModelAdmin):
    list_display = ['id','course_name', 'created_at','updated_at']

@admin.register(Subjects)
class Subject(admin.ModelAdmin):
    list_display = ['id','subject_name','course_id', 'created_at','updated_at']
'''
@admin.register(Attendance)
class Attendace(admin.ModelAdmin):
    list_display = ['id','subject_id','attendance_date','session_year_id','created_at','updated_at']

@admin.register(AttendanceReport)
class AttendaceReport(admin.ModelAdmin):
    list_display = ['id','status','student_id','attendance_id','created_at','updated_at']
'''
@admin.register(SessionYearModel)
class Session(admin.ModelAdmin):
    list_display = ['id','session_start_year','session_end_year' ]

@admin.register(FeedBackStudent)
class FeedBackStudent(admin.ModelAdmin):
    list_display = ['id','student_id','feedback','feedback_reply','created_at','updated_at']

@admin.register(FeedBackStaffs)
class FeedBackStaff(admin.ModelAdmin):
    list_display = ['id','staff_id','feedback','feedback_reply','created_at','updated_at']

@admin.register(StudentResult)
class StudentResult(admin.ModelAdmin):
    list_display = ['id','student_id','subject_id','subject_exam_marks','subject_assignment_marks','created_at','updated_at']

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id','Ename','Edate','branch','photo','date','filetype' ]


    
    
    