from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('Isso aparece quando vc digita http://127.0.0.1:8000')