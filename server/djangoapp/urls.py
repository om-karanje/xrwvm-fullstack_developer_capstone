
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = "djangoapp"

urlpatterns = [
    path("login", views.login_user, name="login"),
    path("logout", views.logout_request, name="logout"),
    path(
        "reviews/<int:dealer_id>",
        views.get_dealer_reviews,
        name="reviews"
    ),
    path("dealers", views.get_dealerships, name="dealers"),
    path("dealer/<int:dealer_id>", views.get_dealer_details, name="dealer-details"),
    path("dealers/state/<str:state>", views.get_dealers_by_state, name="dealers-by-state"),
    path("carmakes", views.get_car_make, name="carmakes"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
