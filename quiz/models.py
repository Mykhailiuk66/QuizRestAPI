from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=500, unique=True)
    
    def __str__(self):
        return self.name
    

class Quiz(models.Model):
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=1000, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class Question(models.Model):
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True, blank=True)
    question = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question[:100]

class Choice(models.Model):
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=False, blank=False)
    choice = models.CharField(max_length=500, blank=False)
    correct_answer = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.choice} - {self.correct_answer}"
    
