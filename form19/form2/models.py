from django.db import models

class UserProfile(models.Model):
    username_or_mobile = models.CharField(max_length=30)
    password=models.CharField(max_length=30)

    def _str_(self):
        return f"{self.user_name_or_mobile}"