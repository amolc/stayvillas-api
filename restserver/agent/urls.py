from django.urls import path
from .views import RegisterAgentViews, AgentViews, LoginViews

urlpatterns = [
    # Agent routes
    path("create-agent/", RegisterAgentViews.as_view()),
    path("login-agent/", LoginViews.as_view()),
    path("get-agent/", AgentViews.as_view()),
    path("update-agent/<int:id>/", AgentViews.as_view()),
    path("delete-agent/<int:id>/", AgentViews.as_view()),
]
