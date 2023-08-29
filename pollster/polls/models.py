"""Module providingFunction printing python version."""
from django.db import models


#  Create your models here.
class Question(models.Model):
    # Specifying fields and max length and it automatically creates an id.
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return f'{self.question_text}'


# connecting choice model with the question, so we link the foriegn and the primary key.
class Choice(models.Model):
    # models.CASCADE=> If a question is deleted all of it's choices is deleted
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.choice_text}'
