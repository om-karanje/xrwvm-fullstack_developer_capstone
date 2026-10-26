
from django.http import JsonResponse
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.csrf import csrf_exempt
import logging
import json

# Get an instance of a logger
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


# Registration view - implement when required
# @csrf_exempt
# def registration(request):
#     pass


# Get dealerships
# def get_dealerships(request):
#     pass


# Get reviews for a dealer
# def get_dealer_reviews(request, dealer_id):
#     pass


# Get dealer details
# def get_dealer_details(request, dealer_id):
#     pass


# Add a review
# def add_review(request):
#     pass
