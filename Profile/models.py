from django.conf import settings
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True)
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='following')
    following = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followers')
