from django.shortcuts import render
from django.http import HttpResponse
from .models import Exam, ExamDetail, ExamScore
from .models import ExamScore
# Create your views here.
def select_exam(request):
    # have to show exist exam
    exam = Exam.objects.all()
    context = {
        'exam' : exam
    }
    
    return render(request, 'check_statistics/select_exam.html', context)

def show_statistics(request, exam_id):
    exam_info = Exam.objects.get(id=exam_id)
    max_score = len(ExamDetail.objects.filter(exam_id = exam_id))
    score_list = ExamScore.objects.filter(exam_id=exam_id)
    
    total = 0
    for score in score_list :
        total += score.score
        
    avg = total/max_score
    
    context = {
        'exam_info' : exam_info,
        'score_list' : score_list,
        'max_score' : max_score,
        'avg' : avg
    }
    
    return render(request, 'check_statistics/show_score.html', context)
