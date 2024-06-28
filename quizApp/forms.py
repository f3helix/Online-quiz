from django import forms
from quizApp.models import *

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ("title", "description")


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ("quiz", "text", "time_limit")

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ("question", "text", "is_correct")