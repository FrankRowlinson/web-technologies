from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from qa.models import *


def test(request, *args, **kwargs):
    return HttpResponse('OK')

def paginate(request, qs):
    page = request.GET.get('page', 1)
    paginator = Paginator(qs, 10)
    page = paginator.get_page(page)
    return page

def new_questions(request):
    new = Question.objects.new()
    page = paginate(request, new)
    context = {
        'page': page,
        }
    return render(request, 'qa/main.html', context=context)

def show_popular(request):
    popular = Question.objects.popular()
    page = paginate(request, popular)
    context = {
        'page': page,
        }
    return render(request, 'qa/popular.html', context=context)
    
def show_question(request, id):
    question = get_object_or_404(Question, id=id)
    answers = Answer.objects.filter(question=question)
    return render(request, 'qa/question.html', context={'question': question, 'answers': answers})


    