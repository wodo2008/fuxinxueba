# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random
import time
import pymongo

from django.http import HttpResponse
from django.shortcuts import render

from qaProgram.models import User_identi_code
from userPhoneVerify.sendMsgUtil import *

# Create your views here.

def getIdentiCode(request):
    mongo_conn = pymongo.MongoClient("mongodb://127.0.0.1:27017")
    user_identi_code = mongo_conn.eke.user_identi_code
    print request
    phoneNum = request.GET.get('phone','')
    apikey = '1cc4281019e663972d7d0f4cca759942'
    identiCode = random.randint(1000,9999)
    text = "【大同学吧】您的验证码是%s" % identiCode
    uicData = user_identi_code.find_one({'phoneNum':phoneNum})
    if not uicData:
        uicData = {}
    uicData['phoneNum'] = phoneNum
    uicData['identiCode'] = identiCode
    uicData['timeStamp'] = time.time()
    uicData['isLegal'] = False
    user_identi_code.save(uicData)    
    print '%s:%s' % (phoneNum,text)
    print send_sms(apikey,text,phoneNum)
    retData = {"success":"Ok","data":""}
    return HttpResponse(json.dumps(retData), content_type='application/json; charset=utf-8')

def submitCode(request):
    retData = {"success": "False", "data": ""}
    phoneNum = request.GET.get('phone', '')
    identiCode = request.GET.get('code', '')
    mongo_conn = pymongo.MongoClient("mongodb://127.0.0.1:27017")
    user_identi_code = mongo_conn.eke.user_identi_code
    uicData = user_identi_code.find_one({'phoneNum':phoneNum})
    print uicData, identiCode
    if uicData and str(uicData.get('identiCode','')) == identiCode:
        retData['success'] = 'Ok'
        uicData['isLegal'] = True
        user_identi_code.save(uicData)
    return HttpResponse(json.dumps(retData), content_type='application/json; charset=utf-8')

def index(request):
    return render(request, 'index.html')

def qrcode(request):
    return render(request, 'qrcode.html')
