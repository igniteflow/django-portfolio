from django.db import models

from tagging.fields import TagField
from tagging.models import Tag
from tinymce import models as tinymce_models
from django_extensions.db.models import TimeStampedModel
 
class PostBase(TimeStampedModel):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    content = tinymce_models.HTMLField()
    slug = models.SlugField(unique=True)
    tags = TagField()
    html = models.BooleanField(default=True)
 
    def get_tags(self):
        return Tag.objects.get_for_object(self)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.title