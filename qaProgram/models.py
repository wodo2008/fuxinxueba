# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Question(models.Model):
    qid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32,default='')
    content = models.TextField()
    status = models.BooleanField(default=False)
    ask_time = models.IntegerField
    asker_openid = models.CharField(max_length=32,default='')
    grad_weixin_id = models.CharField(max_length=32)

class Answer(models.Model):
    aid = models.AutoField(primary_key=True)
    qid = models.ForeignKey("Question",null=True,blank=True)
    content = models.TextField()
    answer_time = models.IntegerField
    grad_weixin_id = models.CharField(max_length=32,default='')

class GradDetail(models.Model):
    gid = models.AutoField(primary_key=True)
    headpic_id = models.IntegerField
    name = models.CharField(max_length=32,default='')
    compay = models.CharField(max_length=32,default='')
    school = models.CharField(max_length=32,default='')
    specialty = models.CharField(max_length=32,default='')
    grad_weixin_id = models.CharField(max_length=32,default='')
