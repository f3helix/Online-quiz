from django.urls import path, include
from .views import *

urlpatterns = [
    path('', QuisListView.as_view(), name= 'quiz_list'),
    # path('add/', CreateQuisView.as_view(), name= 'add'),
]
