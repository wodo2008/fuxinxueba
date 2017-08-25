# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Question(models.Model):
    qid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    content = models.TextField()
    status = models.BooleanField()
    ask_time = models.IntegerField
    asker_openid = models.IntegerField

class Answer(models.Model):
    aid = models.AutoField(primary_key=True)
    qid = models.ForeignKey("Question",null=True,blank=True)
    content = models.TextField()
    answer_time = models.IntegerField
