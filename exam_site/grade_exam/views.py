from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Exam
from .models import ExamDetail
from .models import ExamQuestion
from .models import ExamSubmit
from .models import ExamScore

# Create your views here.
def select_exam(request):
    # have to show exist exam
    exam = Exam.objects.all()
    context = {
        'exam' : exam
    }
    
    return render(request, 'grade_exam/select_exam.html', context)

def grade_exam(request, exam_id):
    # get exam info by exam_id
    exam = Exam.objects.prefetch_related('examdetail_set__examquestion_set').get(id=exam_id)
    exam_submit = Exam.objects.prefetch_related('examsubmit_set').get(id=exam_id)
    temp_submit_list = exam_submit.examsubmit_set.all()
    user_list = []
    for submit in temp_submit_list :
        if submit.user_name not in user_list:
            user_list.append(submit.user_name)
    
    submit_list = []
    for user_name in user_list:
        temp = []
        for submit in temp_submit_list:
            if submit.user_name == user_name:
                temp.append(submit)
                
        submit_list.append(temp)
        
    for user_submit in submit_list:
        exam_score = 0
        do_grade = False
        for i, detail in enumerate(exam.examdetail_set.all()):
            ans = 0
            for j, question in enumerate(detail.examquestion_set.all()):
                ans += (j + 1) * question.ans_yn
                
            if(user_submit[i].is_grade == 1) :
                continue                
            
            if do_grade == False : 
                do_grade = True
            
            user_submit[i].is_grade = 1
            user_submit[i].save()
            
            if int(user_submit[i].exam_ans) == ans:
                exam_score+=1
                    
        if do_grade == True:            
            ExamScore(
                exam_id=exam.id,
                user_name=user_submit[0].user_name,
                score = exam_score
            ).save()
            
    return HttpResponseRedirect('/')