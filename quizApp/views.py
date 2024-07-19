from django.shortcuts import render, redirect, get_object_or_404
from .models import Quiz, Question, Answer
from .forms import QuizForm, QuestionForm, AnswerForm
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.http  import HttpResponseRedirect 



def home(request):
    return render(request, 'base.html')

 


def create_quiz(request):
    if request.method == "POST":
        print(request.POST)
        title = request.POST.get('title')
        description = request.POST.get('description')
   
        quiz = Quiz(title=title, description=description, created_by=request.user)
        quiz.save()
        
    return render (request, 'quizApp/add_quiz.html')

def create_question(request):
    quizs = Quiz.objects.all()

    if request.method == "POST":
        print(request.POST)
        quiz = request.POST.get('quiz')
        text = request.POST.get('text')
        time_limit = request.POST.get('time_limit')
        quiz = get_object_or_404(Quiz, pk=quiz)
        question = Question(quiz=quiz, text=text, time_limit=time_limit)
        question.save()
        
    return render (request, 'quizApp/add_question.html', {"quizs": quizs})

def create_answer(request):
    questions = Question.objects.all()
    print(questions)
    if request.method == "POST":
        print(request.POST)
        question = request.POST.get('question')
        text_answer = request.POST.get('text_answer')
        is_correct = bool(request.POST.get('is_correct'))
        in_correct = bool(request.POST.get('in_correct'))
        question = get_object_or_404(Question, pk=question)
        answer = Answer(question=question, text_answer=text_answer, is_correct=is_correct,in_correct=in_correct)
        answer.save()
        
    return render (request, 'quizApp/add_answers.html', {"questions": questions})


class QuisListView(ListView):
    model = Quiz
    context_object_name = "quizs"
    template_name = "quizApp/quiz_list.html"

class QuestionListView(ListView):
    model = Quiz
    context_object_name = "questions"
    template_name = "quizApp/questions_list.html"

class AnswerListView(ListView):
    model = Quiz
    context_object_name = "answers"
    template_name = "quizApp/answers_list.html"




class CreateQuisView(CreateView):
    model = Quiz
    form_class = QuizForm
    template_name = 'quizApp/add_quiz.html'
    success_url = '/'

class CreateQuestionView(CreateView):
    model = Question
    form_class = QuestionForm
    template_name = 'quizApp/add_question.html'
    success_url = '/'

class CreateAnswersView(CreateView):
    model = Answer
    form_class = AnswerForm
    template_name = 'quizApp/add_answers.html'
    success_url = '/'



    # if request.method == 'POST':
    #     form = QuizForm(request.POST)
    #     if form.is_valid():
    #         quiz = form.save(commit=False)
    #         quiz.created_by = request.user
    #         quiz.save()
    #         return redirect('home')
    # else:
    #     form = QuizForm()
    # return render(request, 'quizApp/add_quiz.html', {'form': form})


# def edit_quiz(request, quiz_id):
#     quiz = get_object_or_404(Quiz, pk=quiz_id) 
#     if request.method == 'POST':
#         form = QuizForm(request.POST, instance=quiz)
#         if form.is_valid():
#             form.save()
#             return redirect('base')
#     else:
#         form = QuizForm(instance=quiz)
#     return render(request, 'quizApp/edit_quiz.html', {'form': form, 'quiz': quiz})


# def delete_quiz(request, quiz_id):
#     quiz = get_object_or_404(Quiz, pk=quiz_id)
#     if request.method == 'POST':
#         quiz.delete()
#         return redirect('base')
#     return render(request, 'quizApp/delete_quiz.html', {'quiz': quiz})




# class QuisDetailView(DetailView):
#     model = Task
#     context_object_name = "task"
#     template_name = "tasktrack_ap/taskdetail.html"


# class QuisUpdateView(UpdateView):
#   model = Task
#   template_name = ""
#   form_class = TaskForm  