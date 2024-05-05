from django.shortcuts import render 
from django.http import HttpResponse
from .models import Feature

def index(request):
    features = Feature.objects.all()
    return render(request, 'index.html', {'features' : features})

def counter(request):
    text = request.POST['text']
    len_text = len(text.split())
    return render(request,'counter.html', {'len_text': len_text})
