# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.

def getIdentiCode(request):
    phoneNum = request.get('phoneNum','')
    retData = {"sucess":"Ok","data":""}
    return HttpResponse(json.dumps(retData), content_type='application/json; charset=utf-8')

def submitCode(request):
    retData = {"sucess": "Ok", "data": ""}
    return HttpResponse(json.dumps(retData), content_type='application/json; charset=utf-8')

