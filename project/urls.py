"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Training import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('admin_Dashboard/', views.admin_Dashboard, name='admin_Dashboard'),
    path('admin_categories/', views.admin_categories, name='admin_categories'),
    path('admin_emp_categories/', views.admin_emp_categories, name='admin_emp_categories'),
    path('admin_courses/', views.admin_courses, name='admin_courses'),
    path('admin_emp_course_list/', views.admin_emp_course_list,name='admin_emp_course_list'),
    path('admin_emp_course_details/', views.admin_emp_course_details,name='admin_emp_course_details'),
    path('admin_emp_profile/', views.admin_emp_profile, name='admin_emp_profile'),
    path('admin_emp_attendance/', views.admin_emp_attendance,name='admin_emp_attendance'),
    path('admin_emp_attendance_show/', views.admin_emp_attendance_show,name='admin_emp_attendance_show'),
    path('admin_task/', views.admin_task, name='admin_task'),
    path('admin_givetask/', views.admin_givetask, name='admin_givetask'),
    path('admin_current_task/', views.admin_current_task,name='admin_current_task'),
    path('admin_previous_task/', views.admin_previous_task,name='admin_previous_task'),
    path('admin_registration_details/', views.admin_registration_details,name='admin_registration_details'), 
    path('admin_attendance/', views.admin_attendance, name='admin_attendance'),
    path('admin_attendance_show/', views.admin_attendance_show,name='admin_attendance_show'),
    path('admin_reported_issues/', views.admin_reported_issues,name='admin_reported_issues'),
    path('admin_emp_reported_detail/', views.admin_emp_reported_detail,name='admin_emp_reported_detail'),
    path('admin_emp_reported_issue_show/', views.admin_emp_reported_issue_show,name='admin_emp_reported_issue_show'),
    path('admin_manager_reported_detail/', views.admin_manager_reported_detail,name='admin_manager_reported_detail'),
    

]
