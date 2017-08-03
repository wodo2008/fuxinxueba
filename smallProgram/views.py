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
    cid = request.GET.get('cid')
    data = Company.objects.filter(cid=cid)
    s = serializer(data)
    response_data = {}
    response_data['data'] = s
    response_data['message'] = 'Ok'
    return HttpResponse(json.dumps(response_data), content_type='application/json; charset=utf-8')

def getExcAlumniList(request):
    pass

def getPushPositionList(request):
    pass

def getExcAlumniDetail(request):
    pass

def getPushPositionDetail(request):
    pass