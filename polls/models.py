from django.db import models

# Create your models here.
class Question(models.Model):
    question_text =
models.Charfield(max_length=20)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    qeustion = models.ForeignKey(Question, on_delete=models.CASCADE)
models.CharFiels(max_length=200)
    votes = models.IntegerField(default=0)
