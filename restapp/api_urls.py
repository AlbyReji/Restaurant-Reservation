from django.urls import include, path
from rest_framework.routers import DefaultRouter

from restapp.api_views import (
    BookingDetailsViewSet,
    ContactDetailsViewSet,
    RestDetailsViewSet,
    UserViewSet,
)

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="api-user")
router.register(r"bookings", BookingDetailsViewSet, basename="api-booking")
router.register(r"contacts", ContactDetailsViewSet, basename="api-contact")
router.register(r"restaurants", RestDetailsViewSet, basename="api-restaurant")

urlpatterns = [
    path("", include(router.urls)),
]
