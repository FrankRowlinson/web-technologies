from django.urls import path
from qa.views import *


urlpatterns = [
    path('', new_questions, name='main'),
    path('login/', LoginPage.as_view(), name='login'),
    path('signup/', SignupPage.as_view(), name='signup'),
    path('question/<int:id>/', show_question, name='question'),
    path('ask/', ask, name='ask'),
    path('popular/', show_popular, name='popular'),
]