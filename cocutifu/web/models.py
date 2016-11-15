from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify


class PostType(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    image = models.CharField(max_length=1023)
    content = models.TextField()
    user = models.ForeignKey(User)
    types = models.ManyToManyField('PostType')
    date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.title)
        super(self.__class__, self).save(*args, **kwargs)

    def get_types_str(self):
        types_str = ''
        for i in self.types.all():
            types_str = '%s, %s' % (i.name, types_str)
        return types_str[:-2]