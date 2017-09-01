# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.db import models
# Create your views here.
from django.http import HttpResponse
from dss.Serializer import serializer
from qaProgram.models import Question,Answer,GradDetail,Picture
from django.forms.models import model_to_dict
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from WXBizMsgCrypt import SHA1
import json
import time
import os
import redis
import requests


def init_redis(host,port,db,password=None):
    if password :
        pool = redis.ConnectionPool(host=host,port=int(port),db=int(db),password=password)
    else:
        pool = redis.ConnectionPool(host=host,port=int(port),db=int(db))
    return redis.Redis(connection_pool=pool)


def get_stu_question_list(request):
    pageNo = int(request.GET.get('pageNo', 1))
    pageSize = int(request.GET.get('pageSize', 10))
    grad_weixin_id = request.GET.get('grad_weixin_id', None)
    if not grad_weixin_id:
        response_data = {}
        response_data['success'] = 'erro'
        response_data['msg'] = 'grad_weixin none'
        return HttpResponse(json.dumps(response_data), content_type='application/json; charset=utf-8')
    data = Question.objects.filter(grad_weixin_id = grad_weixin_id,status=True)
    totalNum = Question.objects.filter(grad_weixin_id=grad_weixin_id,status=True).count()
    paginator = Paginator(data, int(pageSize))
    try:
        pdata = paginator.page(int(pageNo))
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        pdata = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        pdata = paginator.page(paginator.num_pages)
    flist = []
    for d in pdata:
        fdata = {}
        qid = d.qid
        status = d.status
        fdata['qid'] = qid
        fdata['qcontent'] = d.content
        fdata['status'] = status
        if status:
            ansList = Answer.objects.filter(qid=qid)
            fdata['acontent'] = ansList[0].content if ansList else ''
        flist.append(fdata)
    s = serializer(flist)
    response_data = {}
    response_data['data'] = s
    response_data['success'] = 'Ok'
    hasmore = False
    if pageNo * pageSize < totalNum:
        hasmore = True
    response_data['hasmore'] = hasmore
    return HttpResponse(json.dumps(response_data), content_type='application/json; charset=utf-8')


def get_grad_question_list(request):
    pageNo = int(request.GET.get('pageNo', 1))
    pageSize = int(request.GET.get('pageSize', 10))
    grad_weixin_id = request.GET.get('grad_weixin_id', None)
    if not grad_weixin_id:
        response_data = {}
        response_data['success'] = 'erro'
        response_data['msg'] = 'grad_weixin none'
        return HttpResponse(json.dumps(response_data), content_type='application/json; charset=utf-8')
    data = Question.objects.filter(grad_weixin_id=grad_weixin_id,status=False)
    totalNum = Question.objects.filter(grad_weixin_id=grad_weixin_id,status=False).count()
    paginator = Paginator(data, int(pageSize))
    try:
        pdata = paginator.page(int(pageNo))
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        pdata = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        pdata = paginator.page(paginator.num_pages)
    s = serializer(pdata)
    response_data = {}
    response_data['data'] = s
    response_data['success'] = 'Ok'
    hasmore = False
    if pageNo * pageSize < totalNum:
        hasmore = True
    response_data['hasmore'] = hasmore
    return HttpResponse(json.dumps(response_data), content_type='application/json; charset=utf-8')

def get_answer(request):
    qid = request.GET.get('qid', None)
    grad_weixin_id = request.GET.get('grad_weixin_id', None)
    response_data = {}
    if not qid or not grad_weixin_id:
        response_data['success'] = 'erro'
        response_data['msg'] = 'param none'
        return HttpResponse(json.dumps(response_data), content_type='application/json; charset=utf-8')
    try:
        ans = Answer.objects.get(qid=qid, grad_weixin_id=grad_weixin_id)
    except:
        response_data['success'] = 'erro'
        response_data['msg'] = 'no data'
        return HttpResponse(json.dumps(response_data), content_type='application/json; charset=utf-8')
    s = serializer(ans)
    response_data['data'] = s
    response_data['success'] = 'Ok'
    return HttpResponse(json.dumps(response_data), content_type='application/json; charset=utf-8')

def get_question(request):
    qid = request.GET.get('qid', None)
    grad_weixin_id = request.GET.get('grad_weixin_id', None)
    response_data = {}
    if not qid or not grad_weixin_id:
        response_data['success'] = 'erro'
        response_data['msg'] = 'param none'
        return HttpResponse(json.dumps(response_data), content_type='application/json; charset=utf-8')
    try:
        ques = Question.objects.get(qid=qid, grad_weixin_id=grad_weixin_id)
    except:
        response_data['success'] = 'erro'
        response_data['msg'] = 'no data'
        return HttpResponse(json.dumps(response_data), content_type='application/json; charset=utf-8')
    s = serializer(ques)
    response_data['data'] = s
    response_data['success'] = 'Ok'
    return HttpResponse(json.dumps(response_data), content_type='application/json; charset=utf-8')


def getGradDetail(request):
    grad_weixin_id = request.GET.get('grad_weixin_id', None)
    if not grad_weixin_id:
        response_data = {}
        response_data['success'] = 'erro'
        response_data['msg'] = 'param none'
        return HttpResponse(json.dumps(response_data), content_type='application/json; charset=utf-8')
    gdetail = GradDetail.objects.get(grad_weixin_id=grad_weixin_id)
    s = serializer(gdetail)
    response_data = {}
    response_data['data'] = s
    response_data['success'] = 'Ok'
    return HttpResponse(json.dumps(response_data), content_type='application/json; charset=utf-8')


def submit_question(request):
    # request.REQUEST.get('name')
    if request.method == 'POST':
        param_data = json.loads(request.body)
    elif request.method == 'GET':
        signature = request.GET.get("signature");
        timestamp = request.GET.get("timestamp");
        nonce = request.GET.get("nonce");
        echostr = request.GET.get("echostr");
        if checkSignature(signature, timestamp, nonce):
            return HttpResponse(echostr, content_type='application/json; charset=utf-8')
    print 'param_data:',param_data
    mgRedis = init_redis('127.0.0.1', 6379, 0)
    if param_data['MsgType'] == 'event':
        mgRedis.set(param_data['FromUserName'],param_data['SessionFrom'])
        return HttpResponse('success', content_type='application/json; charset=utf-8')
    elif param_data['MsgType'] == 'text':
        content = param_data.get('Content', '')
        ask_time = int(time.time())
        asker_openid = param_data.get('FromUserName', '')
        #grad_weixin_id = param_data.get('ToUserName', '')
        grad_weixin_id = mgRedis.get(param_data.get('FromUserName', ''))
    ques_grad_str = '%s|%s' % (grad_weixin_id,content)
    print 'ques_grad_str:',ques_grad_str
    mgRedis.rpush('ques_grad_mq',ques_grad_str)
    print content,ask_time,asker_openid,grad_weixin_id
    question = Question()
    question.content = content
    question.ask_time = ask_time
    question.asker_openid = asker_openid
    question.grad_weixin_id = grad_weixin_id
    question.save()
    #
    # dic = {}
    # dic['content'] = content
    # dic['ask_time'] = ask_time
    # dic['asker_openid'] = asker_openid
    # dic['grad_weixin_id'] = grad_weixin_id
    # print 'dic:',dic
    # Question.objects.create(dic)

    return HttpResponse('success', content_type='application/json; charset=utf-8')

def submit_answer(request):
    if request.method == 'POST':
        param_data = json.loads(request.body)
    else:
        return HttpResponse('erro,need post', content_type='application/json; charset=utf-8')
    qid = param_data.get('qid', 0)
    content = param_data.get('content', '')
    answer_time = int(time.time())
    grad_weixin_id = param_data.get('grad_weixin_id', '')
    ques = Question.objects.get(qid=qid, grad_weixin_id=grad_weixin_id)
    token_url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential' \
                '&appid=wx5b9b8be6473e5e63&secret=d6b4a2d9c6c517be408d97260384f489'
    token_result = requests.post(token_url)
    print 'token_result:',token_result.text
    access_token = json.loads(token_result.text)['access_token']
    print 'access_token:',access_token
    url = 'https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token=%s' % access_token
    dic = {}
    dic["touser"] = ques.asker_openid
    dic["msgtype"] = "text"
    dic.setdefault("text",{})
    dic["text"]["content"] = "Hello World"
    print 'dic:',dic
    print 'url:',url
    r = requests.post(url, data=json.dumps(dic))
    print 'resp:',r.text
    dic = {}
    dic['qid'] = qid
    dic['content'] = content
    dic['answer_time'] = answer_time
    dic['grad_weixin_id'] = grad_weixin_id
    Answer.objects.create(**dic)
    ques.status = True
    ques.save()
    return HttpResponse('success', content_type='application/json; charset=utf-8')

def getPic(request):
    pname = request.GET.get('pname', None)
    if not pname:
        response_data = {}
        response_data['success'] = 'erro'
        response_data['msg'] = 'param none'
        return HttpResponse(json.dumps(response_data), content_type='application/json; charset=utf-8')
    base_path = '/home/app/fuxinxueba'
    pic_path = os.path.join(base_path,pname)
    image_data = open(pic_path, "rb").read()
    return HttpResponse(image_data, content_type="image/png")

def checkSignature(signature,timestamp,nonce):
    token = 'datongxueba3'
    print signature,timestamp,nonce
    shal = SHA1()
    str = shal.getSHA1(token, timestamp, nonce)
    print str[1]
    if signature == str[1]:
        return True
    else:
        return False



