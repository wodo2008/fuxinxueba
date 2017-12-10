# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from questionnaire.questService import QuestService
import json

# Create your views here.


def save_user_info(request):
    res = {'sucess':'Ok','data':{},'message':''}
    ques_serv = QuestService()
    param = request.GET
    print 'param:',param
    user_id = ques_serv.save_user_info(param)
    res['data']['user_id'] = user_id
    print 'res:',res
    return HttpResponse(json.dump(res),content_type='application/json;charset=utf-8')

def save_ans_info(request):
    res = {'sucess':'Ok','data':{},'message':''}
    ques_serv = QuestService()
    param = request.GET
    print 'param:',param
    ques_serv.save_ans(param)
    print 'res:',res
    return HttpResponse(json.dump(res),content_type='application/json;charset=utf-8')