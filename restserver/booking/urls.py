from django.urls import path
from .views import BookingViews

urlpatterns = [
    path('create-booking/', BookingViews.as_view()),  # POST
    path('get-booking/<int:id>/', BookingViews.as_view()),  # GET by ID
    path('get-bookings/', BookingViews.as_view()),  # GET all (for a specific org_id)
    path('update-booking/<int:id>/', BookingViews.as_view()),  # PATCH
    path('delete-booking/<int:id>/', BookingViews.as_view()),  # DELETE
]
