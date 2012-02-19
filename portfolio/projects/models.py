from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from portfolio.utils.models import TimeStamp

PROJECT_TYPE = (
    ('A', 'Art'),
    ('D', 'Design'),
    ('P', 'Photography'),
    )

class ProjectBase(TimeStamp):
    title       = models.CharField(max_length=200)
    description = models.TextField()
    type = models.CharField(max_length=1, choices=PROJECT_TYPE)

    class Meta:
        abstract = True
    
    def __unicode__(self):
        return self.title
        
class ImageBase(TimeStamp):
    title       = models.CharField(max_length=200)
    description = models.TextField()
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    file        = models.FileField(upload_to='projects')

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.title