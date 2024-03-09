from django.shortcuts import render
from .models import botUser,gmailmalumotlar, instagrammalumotlar
from .serializers import botUserSerializer, gmailSerializer, instaSerializer
from rest_framework.generics import ListCreateAPIView

class BotUsersApiView(ListCreateAPIView):
    queryset = botUser.objects.all()
    serializer_class = botUserSerializer
    
class gmailApiView(ListCreateAPIView):
    queryset = gmailmalumotlar.objects.all()
    serializer_class = gmailSerializer
    
class instaApiView(ListCreateAPIView):
    queryset = instagrammalumotlar.objects.all()
    serializer_class = instaSerializer
    
