from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def question(request, question_id):
    return render(request, 'question.html')
