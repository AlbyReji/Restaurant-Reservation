"""Restreserve URL Configuration"""

from django.contrib import admin
from django.urls import include, path

from restapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # Authentication & Accounts (Registration, Login, Logout)
    path("", include("accounts.urls")),
    # Web Template Views (Class-Based Views)
    path("", views.IndexView.as_view(), name="index"),
    path("ownerhome/", views.OwnerHomeView.as_view(), name="ownerhome"),
    path("userhome/", views.UserHomeView.as_view(), name="userhome"),
    path("bookingstatus/", views.BookingStatusView.as_view(), name="bookingstatus"),
    path(
        "bookingstatus-user/",
        views.BookingStatusUserView.as_view(),
        name="bookingstatus_for_user_url",
    ),
    path("contact/", views.ContactListView.as_view(), name="contact"),
    # Action / Delete Views
    path("delete/<int:id>/", views.DeleteBookingView.as_view(), name="delete_booking"),
    path("delete1/<int:id>/", views.DeleteContactView.as_view(), name="delete_contact"),
    path(
        "delete2/<int:id>/",
        views.DeleteRestDetailsView.as_view(),
        name="delete_restdetails",
    ),
    # Detail / Management Views
    path("edit/<int:id>/", views.RestDetailsUpdateView.as_view(), name="edit_url"),
    path("update/<int:id>/", views.RestDetailsEditView.as_view(), name="update_url"),
    path("Details/", views.AddRestDetailsFormView.as_view(), name="Details"),
    path("Addrestdetails/", views.RestDetailsListView.as_view(), name="Addrestdetails"),
    # REST API Endpoints (Serializers + ViewSets)
    path("api/", include("restapp.api_urls")),
]
