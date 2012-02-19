import urllib2

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
    content = tinymce_models.HTMLField(blank=True, help_text='For RST you can optionally leave this blank and source your RST via a link OR file')
    slug = models.SlugField(unique=True)
    tags = TagField()
    format = models.CharField(max_length=2, choices=FORMATS, default='RS')
    link = models.URLField(blank=True, help_text='Link to RST. For example \'https://raw.github.com/igniteflow/django-portfolio/master/README.rst\'')
    file = models.FileField(upload_to='posts', help_text='Your RST file to be stored as HTML')
 
    def get_tags(self):
        return Tag.objects.get_for_object(self)

    class Meta:
        abstract = True

    def rst2html(self, content):
        w = Writer()
        result = core.publish_parts(content, writer=w)['html_body']
        return '\n'.join(result.split('\n')[1:-2])

    def get_web_resource(self, link):
        return urllib2.urlopen(link).read()

    def get_file_resources(self, file):
        pass

    def is_new_rst_resource(self):
        return not self.id and self.format == 'RS'

    def save(self, *args, **kwargs):
        if self.is_new_rst_resource():
            # @todo add form validation to only allow either link or file, not both
            if self.link:
                self.content = self.get_web_resource(self.link)
            elif self.file:
                self.content = self.file.read()
            self.content = self.rst2html(self.content)
        super(PostBase, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

