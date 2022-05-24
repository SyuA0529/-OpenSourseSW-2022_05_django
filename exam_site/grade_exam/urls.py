from django.urls import path
from . import views

urlpatterns = [
    path('', views.select_exam, name = "select_exam"),
    path('<int:exam_id>/', views.grade_exam, name = 'grade_exam'),
]