# models.py
from django.db import models

class UserProfile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def _str_(self):
        return f"{self.first_name} {self.last_name}"