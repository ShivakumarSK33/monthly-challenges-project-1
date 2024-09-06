from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Dictionary storing the challenges associated with each home item
home_items = {
    "tv": "Eat no meat for the entire month!",
    "fridge": "Walk for at least 20 minutes every day!",
    "washingmachine": "Learn Django for at least 20 minutes every day!",
    "ac": "Eat no meat for the entire month!",
    "sofa": "Walk for at least 20 minutes every day!",
    "mixer": "Learn Django for at least 20 minutes every day!",
    "grinder": "Eat no meat for the entire month!",
    "pc": "Walk for at least 20 minutes every day!",
    "laptop": "Learn Django for at least 20 minutes every day!",
    "wifi": "Eat no meat for the entire month!",
    "bed": "Walk for at least 20 minutes every day!",
    "heater": "Learn Django for at least 20 minutes every day!"
}

# View function to handle requests based on the home item
def house(request, home):
    try:
        challenge_text = home_items[home]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except KeyError:
        return HttpResponseNotFound("<h1>This item is not supported!</h1>")
