from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def question(request):
    return render(request, 'question.html')
