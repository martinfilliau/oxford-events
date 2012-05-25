import datetime

from django.db import models

class Event(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=150)
    comments = models.TextField()
    start_at = models.DateTimeField()

    def has_started(self):
        return self.start_at > datetime.datetime.now()

    def __unicode__(self):
        return self.title
