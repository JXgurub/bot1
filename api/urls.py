from django.urls import path
from .views import BotUsersApiView , gmailApiView,instaApiView

urlpatterns = [
    path("bot", BotUsersApiView.as_view()),
    path("gmail",gmailApiView.as_view()),
    path("insta",instaApiView.as_view()),
]
