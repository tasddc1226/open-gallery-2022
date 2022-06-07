from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Survey(models.Model):
    """설문지는 관리자에 의해 생성"""

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "survey"


class Question(models.Model):
    """
    하나의 설문지에 여러 질문이 존재
    질문의 유형(type)은  Radio(1개), Checkbox(1개 이상), Select(1개) 중 하나
    """

    RADIOBUTTON = 1
    MULTIPLE = 2
    SELECT = 3
    TYPES_CHOICES = [
        (RADIOBUTTON, "RadioButton"),
        (MULTIPLE, "CheckBox"),
        (SELECT, "Select"),
    ]
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=100)
    answer_type = models.IntegerField(
        choices=TYPES_CHOICES, default=RADIOBUTTON
    )

    class Meta:
        db_table = "question"


class Choice(models.Model):
    """
    하나의 질문에는 여러 보기가 존재
    """

    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="choice"
    )
    choice_text = models.CharField(max_length=100)

    class Meta:
        db_table = "choice"


class Submission(models.Model):
    """특정 설문지 질문들에 대한 답변 집합"""

    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    is_complete = models.BooleanField(default=False)

    class Meta:
        db_table = "submission"


class Answer(models.Model):
    """특정 질문에 대한 답변"""

    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    class Meta:
        db_table = "answer"
