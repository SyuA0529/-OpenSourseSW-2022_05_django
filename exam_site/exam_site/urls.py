"""exam_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('show_service.urls')),
    path('create-exam/', include(('create_exam.urls', 'create_exam'), namespace='create_exam')),
    path('take-exam/', include(('take_exam.urls', 'take_exam'), namespace='take_exam')),
    path('grade-exam/', include(('grade_exam.urls', 'grade_exam'), namespace='grade_exam')),
    path('check-statistics/', include(('check_statistics.urls', 'check_statistics'), namespace='check_statistics')),
]