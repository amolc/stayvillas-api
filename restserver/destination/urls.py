# urls.py
from django.urls import path
from .views import DestinationViews

urlpatterns = [
    # path('destinations/', DestinationViews.as_view(), name='destination-list-create'),
    # path('destinations/update-destination/<int:id>/', DestinationViews.as_view(), name='destination-detail'),
    # path('destinations/delete-destination/<int:id>/', DestinationViews.as_view(), name='destination-detail'),
    path("create-destinations/",DestinationViews.as_view()),
    path("destinations/", DestinationViews.as_view()),
    path("update-destinations/<int:id>", DestinationViews.as_view()),
    path("delete-destinations/<int:id>", DestinationViews.as_view()),
]
