# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random
import time

from django.http import HttpResponse
from django.shortcuts import render

from userPhoneAuth.models import unicode_literals
from userPhoneAuth.sendMsgUtil import *


# Create your views here.

def getIdentiCode(request):
    print request
    phoneNum = request.POST.get('phone','')
    apikey = '1cc4281019e663972d7d0f4cca759942'
    identiCode = random.randint(1000,9999)
    text = "【大同学吧】您的验证码是%s" % identiCode
    uic = unicode_literals.objects.get(phoneNum=phoneNum)
    if not uic:
        uic = unicode_literals()
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