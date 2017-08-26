# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from dss.Serializer import serializer
from qaProgram.models import Question,Answer,GradDetail,Picture
from django.forms.models import model_to_dict
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
import time

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
            ans = Answer.objects.get(qid=qid)
            fdata['acontent'] = ans.content if ans else ''
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
    qid = request.GET.get('question_id', None)
    grad_weixin_id = request.GET.get('grad_weixin_id', None)
    if not qid or not grad_weixin_id:
        response_data = {}
        response_data['success'] = 'erro'
        response_data['msg'] = 'param none'
        return HttpResponse(json.dumps(response_data), content_type='application/json; charset=utf-8')
    ans = Answer.objects.get(qid=qid,grad_weixin_id=grad_weixin_id)
    s = serializer(ans)
    response_data = {}
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
    request.REQUEST.get('name')
    content = ''
    ask_time = int(time.time())
    asker_openid = ''
    grad_weixin_id = ''
    dic = {}
    dic['content'] = content
    dic['ask_time'] = ask_time
    dic['asker_openid'] = asker_openid
    dic['grad_weixin_id'] = grad_weixin_id
    models.Question.objects.create(**dic)
    return HttpResponse('success', content_type='application/json; charset=utf-8')

def submit_answer(request):
    qid = 0
    content = ''
    answer_time = int(time.time())
    grad_weixin_id = ''
    dic = {}
    dic['qid'] = qid
    dic['content'] = content
    dic['answer_time'] = answer_time
    dic['grad_weixin_id'] = grad_weixin_id
    models.Answer.objects.create(**dic)
    return HttpResponse('success', content_type='application/json; charset=utf-8')


