# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from dss.Serializer import serializer
from smallProgram.models import Company,Eec_alumni,Push_position
from django.forms.models import model_to_dict
import json

def getCompanyList(request):
    # if request.method == 'GET':
    #     for k in request.query_params:
    #         dict[k] = request.query_params[k]
    # elif request.method == 'POST':
    #     for k in request.data:
    #         dict[k] = request.data[k]
    data = Company.objects.all()
    s = serializer(data)
    response_data = {}
    response_data['data'] = s
    response_data['message'] = 'Ok'
    response_data['pageSize'] = 10
    response_data['pageNo'] = 1
    return HttpResponse(json.dumps(response_data), content_type='application/json; charset=utf-8')

def getExcAlumniList(request):
    cid = request.GET.get('cid')
    data = Eec_alumni.objects.get(cid=cid)
    s = serializer(data)
    response_data = {}
    response_data['data'] = s
    response_data['message'] = 'Ok'
    response_data['pageSize'] = 10
    response_data['pageNo'] = 1
    return HttpResponse(json.dumps(response_data), content_type='application/json; charset=utf-8')


def getPushPositionList(request):
    cid = request.GET.get('cid')
    data = Push_position.objects.get(cid=cid)
    s = serializer(data)
    response_data = {}
    response_data['data'] = s
    response_data['message'] = 'Ok'
    response_data['pageSize'] = 10
    response_data['pageNo'] = 1
    return HttpResponse(json.dumps(response_data), content_type='application/json; charset=utf-8')


def getExcAlumniDetail(request):
    eid = request.GET.get('eid')
    data = Eec_alumni.objects.get(eid=eid)
    s = serializer(data)
    response_data = {}
    response_data['data'] = s
    response_data['message'] = 'Ok'
    response_data['pageSize'] = 10
    response_data['pageNo'] = 1
    return HttpResponse(json.dumps(response_data), content_type='application/json; charset=utf-8')


def getPushPositionDetail(request):
    pid = request.GET.get('pid')
    data = Push_position.objects.get(pid=pid)
    s = serializer(data)
    response_data = {}
    response_data['data'] = s
    response_data['message'] = 'Ok'
    response_data['pageSize'] = 10
    response_data['pageNo'] = 1
    return HttpResponse(json.dumps(response_data), content_type='application/json; charset=utf-8')
