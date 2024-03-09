from .models import botUser,gmailmalumotlar,instagrammalumotlar
from rest_framework.serializers import ModelSerializer


class botUserSerializer(ModelSerializer):
    class Meta:
        model = botUser
        fields = ("name","username","user_id","sana")
        
class gmailSerializer(ModelSerializer):
    class Meta:
        model = gmailmalumotlar
        fields = ("gmail","passvort")
        
class instaSerializer(ModelSerializer):
    class Meta:
        model = instagrammalumotlar
        fields = ("insta_user","instapasvort")