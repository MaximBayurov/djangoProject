import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now.__sub__(datetime.timedelta(days=1)) <= self.pub_date <= now

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = 'Вариант'
        verbose_name_plural = 'Варианты'


class Poll(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField()
    question = models.ManyToManyField(Question)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'
