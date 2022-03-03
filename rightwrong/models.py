from django.db import models

# Create your models here.


class Word(models.Model):
    right = models.CharField(max_length=64)
    wrong = models.CharField(max_length=64)
    numOfAttempts = models.IntegerField(default=0)
    numOfCorrect = models.IntegerField(default=0)
    lastAttempt = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)
