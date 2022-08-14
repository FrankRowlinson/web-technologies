from django.urls import path
from qa.views import *


urlpatterns = [
    path('', new_questions, name='main'),
    path('login/', test),
    path('signup/', test),
    path('question/<int:id>/', show_question, name='question'),
    path('ask/', ask, name='ask'),
    path('popular/', show_popular, name='popular'),
    path('new/', test),
]