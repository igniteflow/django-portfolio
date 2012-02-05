from django.db import models

from django_extensions.db.models import TimeStampedModel

class MessageBase(TimeStampedModel):
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)
    sender = models.EmailField()
    cc_sender = models.BooleanField()
    sent = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "message"
        abstract = True
    
