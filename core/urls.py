from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.event_list, name='event_list'),
    path('quizzes/', views.quiz_list, name='quiz_list'),
    path('quiz/<int:quiz_id>/', views.quiz_attempt, name='quiz_attempt'),
    path('result/<int:submission_id>/', views.quiz_result, name='quiz_result'),
]