from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Course

def submit_score(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        student_name = request.POST.get('student_name')
        subject = request.POST.get('subject')
        score = request.POST.get('score')
        
        return HttpResponse('成績已提交：學號 {}, 姓名 {}, 科目 {}, 分數 {}'.format(
            student_id, student_name, subject, score
        ))
    
    return redirect('catalog')

def home(request):
    courses = Course.objects.all()
    total_score = sum(course.score for course in courses if course.score)
    average_score = round(total_score / len(courses), 2) if courses else 0
    
    context = {
        'courses': courses,
        'average_score': average_score,
    }
    return render(request, 'UI.html', context)

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'course_detail.html', {'course': course})