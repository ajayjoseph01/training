from django.shortcuts import render

# Create your views here.
def admin_Dashboard(request):
    return render(request,'admin/admin_Dashboard.html')

def admin_categories(request):
    return render(request,'admin/admin_categories.html') 

def admin_emp_categories(request):
    return render(request,'admin/admin_emp_categories.html')  

def admin_courses(request):
    return render(request,'admin/admin_courses.html')

def admin_emp_course_list(request):
    return render(request,'admin/admin_emp_course_list.html')

def admin_emp_course_details(request):
    return render(request,'admin/admin_emp_course_details.html')

def admin_emp_profile(request):
    return render(request,'admin/admin_emp_profile.html')

def admin_emp_attendance(request):
    return render(request,'admin/admin_emp_attendance.html')

def admin_emp_attendance_show(request):
    return render(request,'admin/admin_emp_attendance_show.html')

def admin_task(request):
    return render(request,'admin/admin_task.html')

def admin_givetask(request):
    return render(request,'admin/admin_givetask.html')

def admin_current_task(request):
    return render(request,'admin/admin_current_task.html')

def admin_previous_task(request):
    return render(request,'admin/admin_previous_task.html')

def admin_registration_details(request):
    return render(request,'admin/admin_registration_details.html')  

def admin_attendance(request):
    return render(request,'admin/admin_attendance.html') 

def admin_attendance_show(request):
    return render(request,'admin/admin_attendance_show.html')

def admin_reported_issues(request):
    return render(request,'admin/admin_reported_issues.html') 

def admin_emp_reported_detail(request):
    return render(request,'admin/admin_emp_reported_detail.html')

def admin_emp_reported_issue_show(request):
    return render(request,'admin/admin_emp_reported_issue_show.html')

def admin_manager_reported_detail(request):
    return render(request,'admin/admin_manager_reported_detail.html')

