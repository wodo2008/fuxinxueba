# -*- coding: utf-8 -*-
'''
Created on Jul 4, 2017

@author: dzh
'''
import unittest

import requests
from yunpian_python_sdk.model.constant import YP_VERSION, HTTP_CONN_TIMEOUT
from yunpian_python_sdk.ypclient import _YunpianConf

from yunpian_python_sdk.model import constant as YC
from yunpian_python_sdk.ypclient import YunpianClient


class TestYunpianClient(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass

    def test_YunpianConf(self):
        print(__name__)
        conf = _YunpianConf()
        self.assertEqual(conf.conf(YP_VERSION), "v2")
        self.assertEqual(conf.conf(HTTP_CONN_TIMEOUT), "10")

    def test_uri(self):
        url = '{}/{}/{}/{}'.format('https://test-api.yunpian.com', 'v2', 'user', 'get.json')
        self.assertEqual('https://test-api.yunpian.com/v2/user/get.json', url)


    def _test_name(self):
        import sys
        self.assertEqual('tests.test_ypclient', sys.modules[__name__].__name__)

    def _test_requests(self):
        r = requests.get('https://github.com/dzh')
        self.assertEqual(r.status_code, 200)

        r = requests.get('https://www.yunpian.com/')
        self.assertEqual(r.status_code, 200)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    #unittest.main()
    clnt = YunpianClient('1cc4281019e663972d7d0f4cca759942')
    param = {YC.MOBILE: '17317146387', YC.TEXT: '【云片网】您的验证码是1234'}
    r = clnt.sms().single_send(param)




