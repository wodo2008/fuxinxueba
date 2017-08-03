# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def getCompanyList(request):
    if request.method == 'GET':
        for k in request.query_params:
            dict[k] = request.query_params[k]
    elif request.method == 'POST':
        for k in request.data:
            dict[k] = request.data[k]
    BJradio_list = serializers.serialize("json", Company.objects.filter(cid=dict['cid']))
    return HttpResponse(BJradio_list, content_type='application/json; charset=utf-8')