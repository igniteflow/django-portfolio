import datetime

from django.db import models

class TimeStamp(models.Model):
    created     = models.DateTimeField(editable=False)
    modified    = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = datetime.datetime.today()
        self.modified = datetime.datetime.today()
        super(TimeStamp, self).save(*args, **kwargs)

    class Meta:
        abstract = True