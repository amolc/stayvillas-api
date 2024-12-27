from django.urls import path
from .views import *

urlpatterns = [
    # Agent routes
    path("create-agent/", RegisterAgentViews.as_view()),
    path("login-agent/", LoginViews.as_view()),
    path("get-agent/", AgentViews.as_view()),
    path("get-agent/<int:id>/", AgentFilterViews.as_view()),
    path("update-agent/<int:id>/", AgentViews.as_view()),
    path("delete-agent/<int:id>/", AgentViews.as_view()),
    path("forgot-password/", ForgotPasswordView.as_view()),
    path("reset-password/", ResetPasswordView.as_view()),
]
