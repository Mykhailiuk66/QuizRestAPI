from rest_framework import serializers
from .models import Category, Quiz, Question, Choice


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ['creator']
    

    def validate_name(self, value):
        qs = Category.objects.filter(name__iexact=value)

        if qs.exists():
            raise serializers.ValidationError(f"{value} is already a category name")

        return value


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        exclude = ['creator']


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(source='choice_set', many=True, read_only=True)
    type = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Question
        exclude = ['creator', 'created']


    def get_type(self, obj):
        correct_answers = obj.choice_set.filter(correct_answer=True).count()
        total_answers = obj.choice_set.all().count()

        if correct_answers == 1:
            if total_answers > 1:
                type = 'radio'
            elif total_answers == 1:
                type = 'text_answer'
        elif correct_answers > 1:
            type = 'choice'
        else:
            type = None

        return type


class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(source='question_set', many=True, read_only=True)
    
    class Meta:
        model = Quiz
        fields = ['id', 'name', 'category', 'questions']


class QuizzesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Quiz
        fields = ['id', 'name', 'category']

