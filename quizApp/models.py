from django.db import models
from django.contrib.auth.models import User



# class User(models.Model):
#     name = models.CharField(max_length = 200)
#     surname = models.CharField(max_length = 200)





class Quiz(models.Model):
    questions_name = models.CharField(max_length = 200)
    answer_name_1 = models.CharField(max_length = 200)
    answer_name_2 = models.CharField(max_length = 200)
    answer_name_3 = models.CharField(max_length = 200)
    answer_name_4 = models.CharField(max_length = 200)


