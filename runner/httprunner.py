# -*- coding: utf-8 -*-
# @Time : 2020/11/30 19:24 

# @Author : youding

# @File : httprunner.py

# @Software: PyCharm Community Edition


import re
import requests
from requests import Request
from requests.auth import HTTPBasicAuth
from .baserunner import BaseRunner

class HttpRunner(BaseRunner):
    def __init__(self, base_url="127.0.01", verify=False):
        super().__init__(name="Http Runner")
        self.base_url = base_url
        self.http = requests.Session()

        a =  requests.adapters.HTTPAdapter(max_retries=3)
        self.http.mount("http://", a)
        self.http.verify = verify
        self.token = ""
        self.r = None

    def auth(self, uri, user, pwd):
        url = self.base_url + uri
        return self.http.get(url, auth=HTTPBasicAuth(user, pwd))

    def request(self, method, uri, **kwargs):

        url = self.base_url + uri
        try:
            self.r = self.http.request(method=method, url=url, **kwargs)
        except requests.exceptions.ConnectTimeout as e:
            print("HttpRunner Exception: [%s]" % str(e))

        except requests.exceptions.InvalidURL as e:
            print("HttpRunner Exception: [%s]" % str(e))

        return self.r


    @property
    def status_code(self):
        return self.r.status_code

    @property
    def encoding(self):
        '''
        获取编码
        :return:
        '''
        return self.r.encoding


    @property
    def get_headers(self, key=None):
        '''
        获取http响应headers， dict类型
        :param key:
        :return:
        '''
        if key is None:
            return self.r.headers
        else:
            return self.r.headers[key]

    @property
    def json(self):
        '''
        获取json格式的响应内容
        :return:
        '''
        return self.r.json()


    @property
    def text(self):
        '''
        获取原始响应内容
        :return:
        '''
        return self.r.text


    def get_http(self):
        '''
        返回request.session对象， 用于直接 操作requests
        :return:
        '''
        return self.http

    def close(self):
        '''
        断开http连接
        :return:
        '''
        self.http.close()