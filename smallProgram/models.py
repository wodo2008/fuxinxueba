# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Company(models.Model):
    cid = models.AutoField(primary_key=True)
    logo_id = models.IntegerField
    name = models.CharField(max_length=32)
    info = models.TextField()


class Eec_alumni(models.Model):
    eid = models.AutoField(primary_key=True)
    cid = models.ForeignKey("Company",null=True,blank=True)
    name = models.CharField(max_length=32)
    school = models.CharField(max_length=32)
    major = models.CharField(max_length=32)
    head_ortrait_id = models.IntegerField
    brief_intro = models.TextField()
    intro = models.TextField()
    degree = models.CharField(max_length=32)
    interview_info = models.TextField()

class Push_position(models.Model):
    pid = models.AutoField(primary_key=True)
    cid = models.ForeignKey("Company", null=True, blank=True)
    icon_id = models.IntegerField
    name = models.CharField(max_length=32)
    area = models.CharField(max_length=32)
    detail = models.TextField()
    info = models.CharField(max_length=32)
    location = models.CharField(max_length=32)
    publish_time = models.IntegerField
    keywords = models.CharField(max_length=32)
    requirement = models.TextField()
    pluses = models.TextField()