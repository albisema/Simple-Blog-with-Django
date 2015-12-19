from django.db import models
from django.contrib.auth.models import User
import datetime

class BlogPost (models.Model):
    title = models.CharField(max_length=120, blank=True, null=True)
    description = models.TextField(blank=False)
    timestamp = models.DateTimeField('Time', default=datetime.datetime.now)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.title