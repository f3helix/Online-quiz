from django.urls import path, include
from .views import *
from quizApp import views as quizApp

urlpatterns = [
    path('', QuisListView.as_view(), name= 'quiz_list'),
    path('add_quiz/', CreateQuisView.as_view(), name= 'add_quiz'),
    path('add_quiz', quizApp.create_quiz, name = 'add_quiz'),
    # path('base', quizApp.home, name = 'base')
]
