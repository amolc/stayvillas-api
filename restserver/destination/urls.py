# urls.py
from django.urls import path
from .views import DestinationViews

urlpatterns = [
    path('destinations/', DestinationViews.as_view(), name='destination-list-create'),
    path('destinations/<int:id>/', DestinationViews.as_view(), name='destination-detail'),
]
