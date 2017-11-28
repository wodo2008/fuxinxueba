# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random
import time

from django.http import HttpResponse
from django.shortcuts import render

from qaProgram.models import User_identi_code
from userPhoneVerify.sendMsgUtil import *


# Create your views here.

def getIdentiCode(request):
    print request
    phoneNum = request.GET.get('phone','')
    apikey = '1cc4281019e663972d7d0f4cca759942'
    identiCode = random.randint(1000,9999)
    text = "【大同学吧】您的验证码是%s" % identiCode
    #uic = User_identi_code.objects.get(phoneNum=phoneNum)
    #if not None:
    uic = User_identi_code()
    uic.phoneNum = phoneNum
    uic.identiCode = identiCode
    uic.timeStamp = time.time()
    uic.isLegal = False
    uic.save()
    print '%s:%s' % (phoneNum,text)
    print send_sms(apikey,text,phoneNum)
    retData = {"success":"Ok","data":""}
    return HttpResponse(json.dumps(retData), content_type='application/json; charset=utf-8')

def submitCode(request):
    phoneNum = request.POST.get('phoneNum', '')
    identiCode = request.POST.get('identiCode', '')
    retData = {"success": "Ok", "data": ""}
    return HttpResponse(json.dumps(retData), content_type='application/json; charset=utf-8')

def index(request):
    return render(request, 'index.html')

def qrcode(request):
    return render(request, 'qrcode.html')