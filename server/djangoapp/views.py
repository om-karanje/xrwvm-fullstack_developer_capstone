
import os
import json
import logging

from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.csrf import csrf_exempt

logger = logging.getLogger(__name__)


# Login user
@csrf_exempt
def login_user(request):
    if request.method != "POST":
        return JsonResponse(
            {"error": "POST method required"},
            status=405
        )

    try:
        data = json.loads(request.body)
        username = data["userName"]
        password = data["password"]
    except (json.JSONDecodeError, KeyError, TypeError):
        return JsonResponse(
            {"error": "Provide userName and password"},
            status=400
        )

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return JsonResponse({
            "userName": username,
            "status": "Authenticated"
        })

    return JsonResponse({
        "userName": username,
        "status": "Invalid credentials"
    }, status=401)


# Logout user
@csrf_exempt
def logout_request(request):
    if request.method != "POST":
        return JsonResponse(
            {"error": "POST method required"},
            status=405
        )

    logout(request)
    return JsonResponse({"status": "Logged out"})


# Registration placeholder
# Implement registration when required.


# Get dealerships placeholder
def get_dealerships(request):
    dealerships_file = os.path.join(
        settings.BASE_DIR, "database", "data", "dealerships.json"
    )

    try:
        with open(dealerships_file, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (OSError, json.JSONDecodeError):
        logger.exception("Could not load dealerships")
        return JsonResponse(
            {"error": "Could not load dealerships"}, status=500
        )

    return JsonResponse(data)


# Get reviews for a dealer
def get_dealer_reviews(request, dealer_id):
    reviews_file = os.path.join(
        settings.BASE_DIR,
        "database",
        "data",
        "reviews.json"
    )

    try:
        with open(reviews_file, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (OSError, json.JSONDecodeError):
        logger.exception("Could not load dealer reviews")
        return JsonResponse(
            {"error": "Could not load reviews"},
            status=500
        )

    reviews = [
        review for review in data.get("reviews", [])
        if review.get("dealership") == dealer_id
    ]

    return JsonResponse({"reviews": reviews})


# Get dealer details placeholder
def get_dealer_details(request, dealer_id):
    dealerships_file = os.path.join(
        settings.BASE_DIR, "database", "data", "dealerships.json"
    )

    try:
        with open(dealerships_file, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (OSError, json.JSONDecodeError):
        logger.exception("Could not load dealerships")
        return JsonResponse(
            {"error": "Could not load dealerships"}, status=500
        )

    for dealer in data.get("dealerships", []):
        if dealer.get("id") == dealer_id:
            return JsonResponse(dealer)

    return JsonResponse({"error": "Dealer not found"}, status=404)


# Add a review placeholder
# Implement add_review when required.
