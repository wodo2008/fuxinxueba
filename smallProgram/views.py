# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from smallProgram.models import Company,Eec_alumni,Push_position
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
    s = serializers.serialize(data)
    # response_data = {}
    # response_data['data'] = data
    # response_data['message'] = 'Ok'
    return HttpResponse(s, content_type='application/json; charset=utf-8')