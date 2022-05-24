from django.urls import path
from . import views

urlpatterns = [
    path('', views.select_exam, name='select_exam'),
    path('<int:exam_id>/', views.show_statistics, name = 'show_statistics'),
]