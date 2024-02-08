from django.db import models


from django.conf import settings
from django.db import models

class Page(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    moderators = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='moderated_pages')
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='joined_pages')