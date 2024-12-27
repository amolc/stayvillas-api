from django.urls import path
from .views import HolidayViews

urlpatterns = [
    path('create-holiday/', HolidayViews.as_view()),  # POST
    path('get-holiday/<int:id>/', HolidayViews.as_view()),  # GET by ID
    path('get-holiday/', HolidayViews.as_view()),  # GET all
    path('update-holiday/<int:id>/', HolidayViews.as_view()),  # PATCH
    path('delete-holiday/<int:id>/', HolidayViews.as_view()),  # DELETE
]
