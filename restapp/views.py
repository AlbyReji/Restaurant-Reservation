from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, TemplateView, UpdateView

from restapp.forms import bookingdetailsform, contactdetailsform, restdetailsform
from restapp.models import bookingdetails, contactdetails, restdetails


class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """Restricts view access to staff / restaurant owner accounts."""

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, "Access restricted to restaurant staff.")
        return redirect("login")


# ----------------------------------------------------------------------
# 1. Index / Landing Page View
# ----------------------------------------------------------------------
class IndexView(View):
    template_name = "index.html"

    def get(self, request):
        contform = contactdetailsform()
        restaurants = restdetails.objects.all()
        return render(
            request,
            self.template_name,
            {
                "contform": contform,
                "restaurants": restaurants,
            },
        )

    def post(self, request):
        contform = contactdetailsform(request.POST)
        if contform.is_valid():
            contform.save()
            messages.success(request, "Thank you! Your message has been received.")
            return redirect("index")

        restaurants = restdetails.objects.all()
        return render(
            request,
            self.template_name,
            {
                "contform": contform,
                "restaurants": restaurants,
            },
        )


# ----------------------------------------------------------------------
# 4. User Home / Booking View (Customer)
# ----------------------------------------------------------------------
class UserHomeView(LoginRequiredMixin, View):
    template_name = "userhome.html"

    def get(self, request):
        form1 = bookingdetailsform()
        latest_booking = (
            bookingdetails.objects.filter(user=request.user).order_by("-id").first()
        )
        return render(
            request,
            self.template_name,
            {
                "form1": form1,
                "latest_booking": latest_booking,
            },
        )

    def post(self, request):
        form1 = bookingdetailsform(request.POST)
        if form1.is_valid():
            try:
                profile = form1.save(commit=False)
                profile.user = request.user
                profile.save()
                messages.success(
                    request,
                    "Your booking is pending! Check your email or SMS for confirmation.",
                )
                return redirect("userhome")
            except Exception as e:
                messages.error(request, f"Could not save booking: {e}")
        else:
            messages.error(request, "Please correct the booking details.")

        return render(request, self.template_name, {"form1": form1})


# ----------------------------------------------------------------------
# 5. Owner Home View (Staff)
# ----------------------------------------------------------------------
class OwnerHomeView(View):
    template_name = "ownerhome.html"

    def get(self, request):
        return render(request, self.template_name)


# ----------------------------------------------------------------------
# 6. Booking Status View (Staff)
# ----------------------------------------------------------------------
class BookingStatusView(View):
    template_name = "bookingstatus.html"

    def get(self, request):
        booking = bookingdetails.objects.all()
        return render(request, self.template_name, {"booking": booking})


# ----------------------------------------------------------------------
# 7. Booking Status View (Customer / Public restaurant schedule)
# ----------------------------------------------------------------------
class BookingStatusUserView(View):
    template_name = "bookingstatus-user.html"

    def get(self, request):
        cont1 = restdetails.objects.all()
        return render(request, self.template_name, {"cont1": cont1})


# ----------------------------------------------------------------------
# 8. Contact List View (Staff)
# ----------------------------------------------------------------------
class ContactListView(View):
    template_name = "contact.html"

    def get(self, request):
        cont = contactdetails.objects.all()
        return render(request, self.template_name, {"cont": cont})


# ----------------------------------------------------------------------
# 9. Delete Views (Bookings, Contacts, Restaurant Details)
# ----------------------------------------------------------------------
class DeleteBookingView(View):
    def get(self, request, id):
        booking = get_object_or_404(bookingdetails, id=id)
        booking.delete()
        messages.success(request, "Booking successfully removed.")
        return redirect("bookingstatus")


class DeleteContactView(View):
    def get(self, request, id):
        cont = get_object_or_404(contactdetails, id=id)
        cont.delete()
        messages.success(request, "Inquiry successfully deleted.")
        return redirect("contact")


class DeleteRestDetailsView(View):
    def get(self, request, id):
        cont = get_object_or_404(restdetails, id=id)
        cont.delete()
        messages.success(request, "Restaurant timing deleted.")
        return redirect("Addrestdetails")


# ----------------------------------------------------------------------
# 10. Restaurant Details Setup / Management Views
# ----------------------------------------------------------------------
class AddRestDetailsFormView(View):
    """View to add new restaurant hours / specials."""

    template_name = "Details.html"

    def get(self, request):
        contform = restdetailsform()
        return render(request, self.template_name, {"contform": contform})

    def post(self, request):
        contform = restdetailsform(request.POST)
        if contform.is_valid():
            contform.save()
            messages.success(request, "Restaurant details saved successfully.")
            return redirect("Details")
        return render(request, self.template_name, {"contform": contform})


class RestDetailsListView(View):
    """List of all restaurant operational hours / specials."""

    template_name = "Addrestdetails.html"

    def get(self, request):
        cont1 = restdetails.objects.all()
        return render(request, self.template_name, {"cont1": cont1})


class RestDetailsEditView(View):
    """Renders the edit details page."""

    template_name = "editdetails.html"

    def get(self, request, id):
        rest = get_object_or_404(restdetails, id=id)
        return render(request, self.template_name, {"rest": rest})


class RestDetailsUpdateView(View):
    """Processes update submission for restaurant details."""

    template_name = "editdetails.html"

    def post(self, request, id):
        rest = get_object_or_404(restdetails, id=id)
        rest.special = request.POST.get("special", rest.special)
        rest.opentime = request.POST.get("opentime", rest.opentime)
        rest.closetime = request.POST.get("closetime", rest.closetime)
        rest.save()
        messages.success(request, "Details updated successfully.")
        return redirect("Addrestdetails")

    def get(self, request, id):
        rest = get_object_or_404(restdetails, id=id)
        return render(request, self.template_name, {"rest": rest})
