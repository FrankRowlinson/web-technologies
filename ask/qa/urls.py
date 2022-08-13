from django.urls import path
from qa.views import new_questions, show_popular, show_question, test


urlpatterns = [
    path('', new_questions, name='main'),
    path('login/', test),
    path('signup/', test),
    path('question/<int:id>/', show_question, name='question'),
    path('ask/', test),
    path('popular/', show_popular, name='popular'),
    path('new/', test),
]