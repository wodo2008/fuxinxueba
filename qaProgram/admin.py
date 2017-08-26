# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from qaProgram.models import Question,Answer,GradDetail,Picture

# Register your models here.
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(GradDetail)
admin.site.register(Picture)
