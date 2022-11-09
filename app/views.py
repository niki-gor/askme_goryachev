from django.shortcuts import render

from app.models import QUESTIONS


def index(request):
    context = {'questions': QUESTIONS}
    return render(request, 'index.html', context=context)


def question(request, question_id):
    return render(request, 'question.html')
