from django.shortcuts import render,get_object_or_404
from .models import Course

def home(request):
    courses = Course.objects.all()
    scored_courses = []

    for course in courses:
        mid = course.midscore
        final = course.finalscore
        scores = [s for s in (mid, final) if s is not None]
        # 每門課的期中期末平均
        course.total_score = round(sum(scores) / len(scores), 2) if scores else None

        if course.total_score is not None:
            scored_courses.append(course)

    # 所有課程的總平均
    average_score = round(
        sum(c.total_score for c in scored_courses) / len(scored_courses), 2
    ) if scored_courses else 0

    context = {
        'courses': courses,
        'average_score': average_score,
    }
    return render(request, 'UI.html', context)

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if course.midscore is not None and course.finalscore is not None:
        course.total_score = round((course.midscore + course.finalscore) / 2, 2)
    else:
        course.total_score = None
    return render(request, 'course_detail.html', {'course': course})

