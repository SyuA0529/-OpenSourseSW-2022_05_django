from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Exam, ExamDetail, ExamQuestion
from django.urls import reverse
import json

# Create your views here.
def create_exam(request) :
    return render(request, 'create_exam/create_exam.html')

def submit_exam_info(request):
    request = json.loads(request.body)
    Exam(type = request['type'], name = request['name'], register = request['register']).save()
    cur_exam = Exam.objects.filter(type = request['type'], name = request['name'], register = request['register']).get()
    return JsonResponse({'exam_id':cur_exam.id}, status = 200)

def create_question(request, exam_id, question_id) :
    context = {
        'exam_id' : exam_id,
        'question_id' : question_id,    
    }
    return render(request, 'create_exam/create_question.html', context)

def submit_question(request) :
    try :
        request = json.loads(request.body)
        
    except :
        return JsonResponse({'message':'SUCCESS'}, status = 200)
    
    ExamDetail(exam_id = request['exam_id'],
           exam_num = request['question_id'],
           exam_subject = request['subject'],
           exam_contents = request['contents']).save()
    
    cur_exam_detail = ExamDetail.objects.filter(exam_id = request['exam_id'], exam_num = request['question_id']).get()
    ans_index = request['answer']
    for i in range(1, 6) :
        ans = 0
        print("i = " + str(i), "ans = " + str(ans_index))
        
        if int(ans_index) == i:
            print("it's ans!")
            ans = 1
        
        ExamQuestion(exam_detail_id = cur_exam_detail.id,
                     question_num = i,
                     question_contents = request['question'][i-1],
                     ans_yn = ans).save()
        
    return JsonResponse({'message':"SUCCESS"}, status = 200)