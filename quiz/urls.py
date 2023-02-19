from django.urls import path
from . import views


urlpatterns = [
    path('categories/', views.CategoryListCreateAPIView.as_view()),
    path('categories/<int:pk>/', views.CategoryRetrieveUpdateDestroyAPIView.as_view()),

    path('quizzes/', views.QuizListCreateAPIView.as_view()),
    path('quizzes/<int:pk>/', views.QuizRetrieveUpdateDestroyAPIView.as_view()),

    path('questions/', views.QuestionListCreateAPIView.as_view()),
    path('questions/<int:pk>/', views.QuestionRetrieveUpdateDestroyAPIView.as_view()),
    
    path('choices/', views.ChoiceListCreateAPIView.as_view()),
    path('choices/<int:pk>/', views.ChoiceRetrieveUpdateDestroyAPIView.as_view()),

]
