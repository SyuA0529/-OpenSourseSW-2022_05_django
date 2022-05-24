from audioop import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Prefetch
from .models import Exam
from .models import ExamDetail
from .models import ExamQuestion
from .models import ExamSubmit
import json
# Create your views here.

def select_exam(request):
    # have to show exist exam
    exam = Exam.objects.all()
    context = {
        'exam' : exam
    }
    
    return render(request, 'take_exam/select_exam.html', context)

def show_exam(request, exam_id):
    # get exam id from user
    exam = Exam.objects.prefetch_related('examdetail_set__examquestion_set').get(id=exam_id)
    
    context = {
        'exam': exam
    }
    
    return render(request, 'take_exam/take_exam.html', context)

def submit_exam(request):
    request = json.loads(request.body)
    try :
        exam_submit = ExamSubmit.objects.filter(user_name=request['user_id'])
        exam_submit[0]
        return JsonResponse({'message':'EXIST'}, status = 200)
    
    except :    
        answer = request['answer'].split(',')
        print(answer)
        for i, var in enumerate(answer):
            if var:
                ExamSubmit(exam_id=request['exam_id'], 
                           exam_detail_num=(i+1), 
                           user_name=request['user_id'],
                           exam_ans=var,
                           is_grade = 0).save()

        return JsonResponse({'message':"SUCCESS"}, status = 200)