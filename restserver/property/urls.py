# django
from django.urls import path

# custom
from .views import PropertyViews

urlpatterns = [
    
    # property
    path("create-property/", PropertyViews.as_view()),
    path("get-property/", PropertyViews.as_view()),
    path("update-property/", PropertyViews.as_view()),
    path("delete-property/", PropertyViews.as_view()),
]