from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.select_exam, name = 'select_exam'),
    path('<int:exam_id>/', views.show_exam, name = 'show_exam'),
    path('submit', views.submit_exam, name = 'submit_exam'),
]