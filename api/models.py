from django.db import models

class botUser(models.Model):
    user_id = models.CharField(max_length = 120)
    name = models.CharField(max_length = 120)
    username = models.CharField(max_length = 120 , null =True ,blank = True)
    sana = models.DateTimeField(auto_now_add = True)
    
    def __str__ (self):
        return str(self.name)
    
    
class gmailmalumotlar(models.Model):
    gmail = models.CharField(max_length = 120)
    passvort = models.CharField(max_length =120)
    
    def __str__(self):
        return str(self.gmail)
    
class instagrammalumotlar(models.Model):
    insta_user = models.CharField(max_length = 120)
    instapasvort = models.CharField(max_length = 120)
    def __str__(self):
        return str(self.insta_user)