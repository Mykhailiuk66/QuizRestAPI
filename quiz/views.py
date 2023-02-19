from django.shortcuts import render
from rest_framework import generics, permissions, authentication, pagination
from rest_framework.decorators import api_view 
from rest_framework.response import Response

from .models import Category, Quiz, Question, Choice
from . import serializers


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(creator=user)

class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    

class QuizListCreateAPIView(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = serializers.QuizzesSerializer

    def get_queryset(self):
        category_id = self.request.query_params.get('category_id')
        if category_id:
            queryset = Quiz.objects.filter(category=category_id)
        else:
            queryset = super().get_queryset()

        return queryset


    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(creator=user)


class QuizRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quiz.objects.all()
    serializer_class = serializers.QuizSerializer
    


class QuestionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = serializers.QuestionSerializer
    
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(creator=user)

        
class QuestionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = serializers.QuestionSerializer
    

class ChoiceListCreateAPIView(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = serializers.ChoiceSerializer
    permission_classes = [permissions.DjangoModelPermissions]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(creator=user)

        
class ChoiceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Choice.objects.all()
    serializer_class = serializers.ChoiceSerializer
    permission_classes = [permissions.DjangoModelPermissions]

