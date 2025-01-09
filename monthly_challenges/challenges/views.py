from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


# def january(request):
#     return HttpResponse("Eat no meat for the entire month!")
# def february(request):
#     return HttpResponse("Walk for at least 20 minutes every day!")


def monthly_challenge_by_number(request, month):
    return HttpResponse(month)


def monthly_challenges(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "Eat no meat for the entire month!"
    elif month == "february":
        challenge_text = "Walk for at least 20 minutes every day!"
    elif month == "march":
        challenge_text = "Learn Django for at least 20 minutes every day"
    else:
        return HttpResponseNotFound("Month not found!")
    return HttpResponse(challenge_text)
