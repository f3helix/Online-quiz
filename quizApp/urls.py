from django.urls import path, include
from .views import *
from quizApp import views as quizApp

urlpatterns = [
    path('', QuisListView.as_view(), name= 'quiz_list'),
    path('add_quiz/', CreateQuisView.as_view(), name= 'add_quiz'),
    path('add_question/', CreateQuestionView.as_view(), name= 'add_question'),
    path('add_quiz', quizApp.create_quiz, name = 'add_quiz'),
    path('add_question', quizApp.create_question, name = 'add_question'),


    path('questions_list', QuestionListView.as_view(), name = 'questions_list')
]
