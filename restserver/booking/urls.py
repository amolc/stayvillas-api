from django.urls import path
from .views import BookingViews, EventBookingViews

urlpatterns = [
    path('create-booking/', BookingViews.as_view()),  # POST
    path('get-booking/<int:id>/', BookingViews.as_view()),  # GET by ID
    path('get-bookings/', BookingViews.as_view()),  # GET all (for a specific org_id)
    path('update-booking/<int:id>/', BookingViews.as_view()),  # PATCH
    path('delete-booking/<int:id>/', BookingViews.as_view()),  # DELETE

    path('create-event-booking/', EventBookingViews.as_view()),  # POST
    path('get-event-booking/<int:id>/', EventBookingViews.as_view()),  # GET by ID
    path('get-event-bookings/', EventBookingViews.as_view()),  # GET all (for a specific org_id)
    path('update-event-booking/<int:id>/', EventBookingViews.as_view()),  # PATCH
    path('delete-event-booking/<int:id>/', EventBookingViews.as_view()),  # DELETE
]
