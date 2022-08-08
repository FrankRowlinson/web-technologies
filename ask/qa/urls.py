from django.urls import path
from qa.views import test


urlpatterns = [
    path('', test),
    path('signup/', test),
    path('question/<int:id>/', test),
    path('ask/', test),
    path('popular/', test),
    path('new/', test),
]