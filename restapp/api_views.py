from django.contrib.auth.models import User
from rest_framework import permissions, viewsets

from restapp.models import bookingdetails, contactdetails, restdetails
from restapp.serializers import (
    BookingDetailsSerializer,
    ContactDetailsSerializer,
    RestDetailsSerializer,
    UserSerializer,
)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint to view users."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class BookingDetailsViewSet(viewsets.ModelViewSet):
    """API endpoint for table bookings."""

    queryset = bookingdetails.objects.all()
    serializer_class = BookingDetailsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return bookingdetails.objects.all()
        return bookingdetails.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ContactDetailsViewSet(viewsets.ModelViewSet):
    """API endpoint for contact inquiries."""

    queryset = contactdetails.objects.all()
    serializer_class = ContactDetailsSerializer

    def get_permissions(self):
        if self.action in ["create"]:
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]


class RestDetailsViewSet(viewsets.ModelViewSet):
    """API endpoint for restaurant opening hours and specials."""

    queryset = restdetails.objects.all()
    serializer_class = RestDetailsSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]
