from django.db import models

from tagging.fields import TagField
from tagging.models import Tag
from tinymce import models as tinymce_models
from django_extensions.db.models import TimeStampedModel
from docutils import core
from docutils.writers.html4css1 import Writer
 
class PostBase(TimeStampedModel):

    FORMATS = (
        ('RS', 'rst'),
        ('HT', 'html'),
    )

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    content = tinymce_models.HTMLField()
    slug = models.SlugField(unique=True)
    tags = TagField()
    format = models.CharField(max_length=2, choices=FORMATS, default='RS')
 
    def get_tags(self):
        return Tag.objects.get_for_object(self)

    class Meta:
        abstract = True

    def rst2html(self, content):
        w = Writer()
        result = core.publish_parts(content, writer=w)['html_body']
        return '\n'.join(result.split('\n')[1:-2])

    def save(self, *args, **kwargs):
        if self.format == 'RS':
            self.content = self.rst2html(self.content)
        super(PostBase, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title
