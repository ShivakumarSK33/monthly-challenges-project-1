# from django.shortcuts import render
# from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# monthly_challenge = {
#     "January": "Eat no meat",
#     "February": "Walk for 20 mins",
#     "March": "Learn Python",
#     "April": "Take some break",
#     "May": "Workout some problems",
#     "June": "Revise once",
#     "July": "Learn java",
#     "August": "Learn django",
#     "September": "Take 20 mins break",
#     "October": "Learn other questions",
#     "November": "Walk for 40 mins",
#     "December": "Revise"
# }

# def monthly_challenge_by_number(request, month):
#     return HttpResponse(month)

# def monthly_challenge(request, month):
#     try:
#         challenge_text = monthly_challenge(month)
#     except:
#         return HttpResponseNotFound("This month is not supported")
#     return HttpResponse(challenge_text)

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": "Learn Django for at least 20 minutes every day!"
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f'<li><a href="{month_path}">{capitalized_month}</a></li>'

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months) or month < 1:
        return HttpResponseNotFound("<h1>Invalid month</h1>")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) 
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except KeyError:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
