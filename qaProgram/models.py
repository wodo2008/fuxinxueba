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
    class Meta:
      ordering = ['-ask_time']
    def __str__(self):
        return self.title

class Answer(models.Model):
    aid = models.AutoField(primary_key=True)
    qid = models.IntegerField(default=0)
    content = models.TextField()
    answer_time = models.IntegerField(default=0)
    grad_weixin_id = models.CharField(max_length=32,default='')
    class Meta:
      ordering = ['-answer_time']
    def __str__(self):
        return self.content

class GradDetail(models.Model):
    gid = models.AutoField(primary_key=True)
    #avatar = models.ForeignKey("Picture",null=True,blank=True)
    avatar = models.ImageField(upload_to='img')
    name = models.CharField(max_length=32,default='')
    company = models.CharField(max_length=32,default='')
    school = models.CharField(max_length=32,default='')
    specialty = models.CharField(max_length=32,default='')
    grad_weixin_id = models.CharField(max_length=32,default='')
    def __str__(self):
        return self.name


class Picture(models.Model):
    pid = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to='img')
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

