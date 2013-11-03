# -*- coding: utf-8 -*-

from django.db import models
from django.contrib import admin

class Parameter(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField()

    def __unicode__(self):
        return self.name

admin.site.register(Parameter)
