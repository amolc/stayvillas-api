# django
from django.urls import path

# custom
from .views import RegisterCustomerViews, AuthenticateUser, CustomerViews

urlpatterns = [
    # property
    path("create-customer/", RegisterCustomerViews.as_view()),
    path("login-customer/", AuthenticateUser.as_view()),
    path("get-customer/", CustomerViews.as_view()),

]