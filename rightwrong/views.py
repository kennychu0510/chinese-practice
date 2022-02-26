from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Word
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import random
from django.utils import timezone

# Create your views here.


def index(request):
    # select 10 words from database ordered by least number of correct attempts
    words = list(Word.objects.order_by('numOfCorrect')[:10])
    # shuffle the 10 words
    random.shuffle(words)

    # Random sort with weighting, same words may be selected
    # allWords = list(Word.objects.all())
    # weight_list = Word.objects.values('numOfAttempts')
    # weighting = []
    # for x in weight_list:
    #     if x['numOfAttempts'] == 0:
    #         weighting.append(1)
    #     else:
    #         weighting.append(1/(x['numOfAttempts']))
    # # Pick 10 random words based on number of attempts (least attempted words get picked more likely)
    # words = random.choices(allWords, weights=weighting, k=10)
    return render(request, "home.html", {
        "words": words
    })


@ csrf_exempt
def updateScore(request, word_id):
    if request.method == "PUT":
        feedback = json.loads(request.body)
        attempts = Word.objects.get(pk=word_id)
        if feedback.get("correct") == True:
            attempts.numOfCorrect += 1

        attempts.numOfAttempts += 1
        attempts.save()
    return HttpResponse(status=204)


def statistics(request, sort):
    print(sort)
    if sort == 'id':
        words = Word.objects.all()
    elif sort == 'correct':
        words = Word.objects.order_by('-numOfCorrect')
    elif sort == 'attempts':
        words = Word.objects.order_by('-lastAttempt')
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
