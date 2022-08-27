from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator
from qa.models import *
from qa.forms import *


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
        answer = Answer(author=request.user)
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            form.save()
            url = question.get_absolute_url()
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm(initial={'question': question.pk})
    answers = Answer.objects.filter(question=question)
    context={'question': question, 'answers': answers, 'form': form}
    return render(request, 'qa/question.html', context=context)

@login_required
def ask(request):
    if request.method == "POST":
        question = Question(author=request.user)
        form = AskForm(request.POST, instance=question)
        if form.is_valid():
            post = form.save()
            url = post.get_absolute_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'qa/ask.html', {'form': form})


class SignupPage(CreateView):
    form_class = UserSignupForm
    template_name = 'qa/signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main')


class LoginPage(LoginView):
    form_class = AuthenticationForm
    template_name = 'qa/login.html'

    def get_success_url(self) -> str:
        return reverse_lazy('main')


    