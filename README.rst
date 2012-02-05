django-portfolio
================

A simple set of abstract models and functionality to speed up the development of a portfolio type site.  There are
models to provide functionality for:


1. Contact form
2. Blog
3. Projects (which have images)

Installation
------------

Install with::

    pip install django-portfolio

Add 'portfolio' to your INSTALLED_APPS and extend as required.  Here are some example usages assuming that you
have created three skeleton apps in your project called contact, blog and project:

Contact
-------

models.py::

    from portfolio.contact.models import MessageBase

    class Message(MessageBase):
        pass

admin.py::

    from django.contrib import admin

    from contact.models import Message

    class MessageAdmin(admin.ModelAdmin):
        readonly_fields = ['subject', 'message', 'sender', 'cc_sender', 'sent']
        date_hierarchy = 'sent'
        list_display = ('subject', 'message', 'sender', 'sent')
        list_filter = ('sent','sender')
        search_fields = ['subject', 'sender', 'message']

    admin.site.register(Message, MessageAdmin)


Blog
----

models.py::

    from portfolio.blog.models import PostBase

    class Post(PostBase):
        pass

admin.py::

    from django.contrib import admin

    from blog.models import Post

    admin.site.register(Post)

Projects
--------

models.py::

    from portfolio.projects.models import ProjectBase, ImageBase

    class Project(ProjectBase):
        pass

    class Image(ImageBase):
        pass

admin.py::

    from django.contrib import admin
    from django.contrib.contenttypes import generic

    from projects.models import Project, Image

    class ImageInline(generic.GenericTabularInline):
        model = Image

    class ProjectAdmin(admin.ModelAdmin):
        inlines = [
            ImageInline,
            ]

    admin.site.register(Project, ProjectAdmin)


Update your database, fire up the admin and inspect the models.  You are now free to customise at will.

Dependencies
------------

-   django-extensions   TimeStampedModel is used as the base class for all models
-   django-tagging      Used in blog posts. You may also want to add this to Projects