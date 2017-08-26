# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Question(models.Model):
    qid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32,default='')
    content = models.TextField()
    status = models.BooleanField(default=False)
    ask_time = models.IntegerField(default=0)
    asker_openid = models.CharField(max_length=32,default='')
    grad_weixin_id = models.CharField(max_length=32)

class Answer(models.Model):
    aid = models.AutoField(primary_key=True)
    qid = models.ForeignKey("Question",null=True,blank=True)
    content = models.TextField()
    answer_time = models.IntegerField(default=0)
    grad_weixin_id = models.CharField(max_length=32,default='')

class GradDetail(models.Model):
    gid = models.AutoField(primary_key=True)
    #avatar = models.ForeignKey("Picture",null=True,blank=True)
    avatar = models.ImageField(upload_to='img')
    name = models.CharField(max_length=32,default='')
    company = models.CharField(max_length=32,default='')
    school = models.CharField(max_length=32,default='')
    specialty = models.CharField(max_length=32,default='')
    grad_weixin_id = models.CharField(max_length=32,default='')

class Picture(models.Model):
    pid = models.AutoField(primary_key=True)
    img = models.ImageField()
    name = models.CharField(max_length=20)

