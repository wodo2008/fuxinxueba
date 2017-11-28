# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class UserIdentiCode(models.Model):
    id = models.AutoField(primary_key=True)
    phoneNum = models.CharField(max_length=32,default='')
    identiCode = models.CharField(max_length=32,default='')
    timeStamp = models.TimeField
    isLegal = models.BooleanField
    def __str__(self):
        return self.phoneNum