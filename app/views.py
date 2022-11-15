from django.shortcuts import render

from app.models import questions


def index(request):
    context = {'questions': questions.values()}
    return render(request, 'index.html', context=context)


def question(request, question_id):
    context = {
        'question': questions[question_id]
    }
    return render(request, 'question.html', context=context)


def ask(request):
    return render(request, 'ask.html')
