# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from dss.Serializer import serializer
from qaProgram.models import Question,Answer
from django.forms.models import model_to_dict
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json

def get_stu_question_list(request):
    pageNo = request.GET.get('pageNo', 1)
    pageSize = request.GET.get('pageSize', 10)

    data = Question.objects.all()
    totalNum = Question.objects.filter().count()
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
        if status:
            ans = Answer.objects.get(qid=qid)
            fdata['acontent'] = ans.content if ans else ''
    s = serializer(fdata)
    response_data = {}
    response_data['data'] = s
    response_data['success'] = 'Ok'
    response_data['totalNum'] = totalNum
    response_data['totalPage'] = totalNum / pageSize + 1
    response_data['currentPage'] = pageNo
    return HttpResponse(json.dumps(response_data), content_type='application/json; charset=utf-8')