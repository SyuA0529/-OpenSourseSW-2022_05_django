from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_exam, name='create_exam'),
    path('submit_exam_info', views.submit_exam_info, name = "submit_exam_info"),
    path('<int:exam_id>/<int:question_id>', views.create_question, name="create_question"),
    path('submit_question',views.submit_question, name='submit_question' )
]