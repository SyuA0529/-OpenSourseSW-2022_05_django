from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show_service(request):
    return render(request, 'show_service/index.html')