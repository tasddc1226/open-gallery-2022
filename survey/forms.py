from django import forms
from .models import Survey, Question, Choice


class SurveyCreateForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = [
            "title",
            "description",
        ]


class QuestionCreateForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["question_text", "answer_type"]


class ChoiceCreateForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ["choice_text"]
