from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from qa.models import *
from qa.forms import *
 

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
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            form.save()
            url = question.get_absolute_url()
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm(initial={'question': question.pk})
    answers = Answer.objects.filter(question=question)
    context={'question': question, 'answers': answers, 'form': form}
    return render(request, 'qa/question.html', context=context)

def ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            post = form.save()
            url = post.get_absolute_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'qa/ask.html', {'form': form})



    