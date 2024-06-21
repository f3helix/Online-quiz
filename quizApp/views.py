from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from quizApp.models import *
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.http  import HttpResponseRedirect 


def index(request):
    return render(request, 'quizApp/base.html')


def add_quiz(request):
    if request.method == "POST":
        questions_name = request.POST.get('questions_name')
        answer_name_1 = request.POST.get('answer_name_1')
        answer_name_2 = request.POST.get('answer_name_2')
        answer_name_3 = request.POST.get('answer_name_3')
        answer_name_4 = request.POST.get('answer_name_4')

        
        addtask = Quiz(questions_name=questions_name, 
                       answer_name_1=answer_name_1, 
                       answer_name_2=answer_name_2, answer_name_3=answer_name_3,
                       answer_name_4=answer_name_4)
        addtask.save()
        
    return render (request, 'event/index.html')



# class LoginView(View):
#     template_name = 'quizApp/login.html'

#     def get(self, request):
#         form = AuthenticationForm()
#         return render(request, self.template_name, {'form': form})

#     def post(self, request):
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('home')  

# class LogoutView(View):
#     def get(self, request):
#         logout(request)
#         return redirect('login')

# class RegisterView(View):
#     template_name = 'quizApp/register.html'

#     def get(self, request):
#         form = UserCreationForm()
#         return render(request, self.template_name, {'form': form})

#     def post(self, request):
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home') 

