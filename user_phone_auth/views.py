# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import json
from sendMsgUtil import *
import random
import time
from user_phone_auth.models import UserIdentiCode
# Create your views here.

def getIdentiCode(request):
    phoneNum = request.POST.get('phoneNum','')
    apikey = '1cc4281019e663972d7d0f4cca759942'
    identiCode = random.randint(1000,9999)
    text = "【大同学吧】您的验证码是%s" % identiCode

    uic = UserIdentiCode.get(phoneNum=phoneNum)
    if not uic:
        uic = UserIdentiCode()
    uic.phoneNum = phoneNum
    uic.identiCode = identiCode
    uic.timeStamp = time.time()
    uic.isLegal = False
    uic.save()
    send_sms(apikey,text,phoneNum)
    retData = {"sucess":"Ok","data":""}
    return HttpResponse(json.dumps(retData), content_type='application/json; charset=utf-8')

def submitCode(request):
    phoneNum = request.POST.get('phoneNum', '')
    identiCode = request.POST.get('identiCode', '')

    retData = {"sucess": "Ok", "data": ""}

    return HttpResponse(json.dumps(retData), content_type='application/json; charset=utf-8')

def index(request):
    return render(request, 'index.html')