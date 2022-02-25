from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Word
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import random

# Create your views here.


def index(request):
    words = list(Word.objects.all())
    random.shuffle(words)
    words = words[0:10]
    return render(request, "home.html", {
        "words": words
    })


@csrf_exempt
def updateScore(request, word_id):
    if request.method == "PUT":
        feedback = json.loads(request.body)
        attempts = Word.objects.get(pk=word_id)
        if feedback.get("correct") == True:
            attempts.numOfCorrect += 1

        attempts.numOfAttempts += 1
        attempts.save()
    return HttpResponse(status=204)


def statistics(request):
    words = Word.objects.all()
    return render(request, "statistics.html", {
        "words": words
    })


def reset(request):
    words = Word.objects.all()

    for word in words:
        word.numOfCorrect = 0
        word.numOfAttempts = 0
        word.save()

    return statistics(request)
