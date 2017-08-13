# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from dss.Serializer import serializer
from smallProgram.models import Company,Eec_alumni,Push_position
from django.forms.models import model_to_dict
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json

def getCompanyList(request):
    # if request.method == 'GET':
    #     for k in request.query_params:
    #         dict[k] = request.query_params[k]
    # elif request.method == 'POST':
    #     for k in request.data:
    #         dict[k] = request.data[k]

    pageNo = request.GET.get('pageNo')
    pageSize = request.GET.get('pageSize')

    data = Company.objects.all()
    totalNum = Company.objects.get(cid=cid).count()
    paginator = Paginator(data, int(pageSize))

    try:
        pdata = paginator.page(pageNo)
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
    response_data['totalNum'] = totalNum
    response_data['totalPage'] = totalNum / pageSize + 1
    response_data['currentPage'] = pageNo
    return HttpResponse(json.dumps(response_data), content_type='application/json; charset=utf-8')

def getExcAlumniList(request):
    cid = request.GET.get('cid')
    pageNo = request.GET.get('pageNo')
    pageSize = request.GET.get('pageSize')
    data = Eec_alumni.objects.get(cid=cid)
    totalNum = Eec_alumni.objects.get(cid=cid).count()
    paginator = Paginator(data, int(pageSize))
    try:
        pdata = paginator.page(pageNo)
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
    response_data['totalNum'] = totalNum
    response_data['totalPage'] = totalNum / pageSize + 1
    response_data['currentPage'] = pageNo
    return HttpResponse(json.dumps(response_data), content_type='application/json; charset=utf-8')


def getPushPositionList(request):
    cid = request.GET.get('cid')
    pageNo = request.GET.get('pageNo')
    pageSize = request.GET.get('pageSize')
    data = Push_position.objects.get(cid=cid)
    totalNum = Push_position.objects.get(cid=cid).count()
    paginator = Paginator(data, int(pageSize))
    try:
        pdata = paginator.page(pageNo)
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
    response_data['totalNum'] = totalNum
    response_data['totalPage'] = totalNum / pageSize + 1
    response_data['currentPage'] = pageNo
    return HttpResponse(json.dumps(response_data), content_type='application/json; charset=utf-8')


def getExcAlumniDetail(request):
    eid = request.GET.get('eid')
    data = Eec_alumni.objects.get(eid=eid)
    s = serializer(data)
    response_data = {}
    response_data['data'] = s
    response_data['success'] = 'Ok'
    return HttpResponse(json.dumps(response_data), content_type='application/json; charset=utf-8')


def getPushPositionDetail(request):
    pid = request.GET.get('pid')
    data = Push_position.objects.get(pid=pid)
    s = serializer(data)
    response_data = {}
    response_data['data'] = s
    response_data['success'] = 'Ok'
    return HttpResponse(json.dumps(response_data), content_type='application/json; charset=utf-8')
