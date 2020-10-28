# -*- coding: utf-8 -*-
# @Time : 2020/10/26 15:29 

# @Author : youding

# @File : runner.py

# @Software: PyCharm Community Edition

"""
基类
"""

import requests
from requests import Request
from requests.auth import HTTPBasicAuth


class Runner(object):
    def __init__(self, name="Base Runner"):
        self.name = name




class HttpRunner(Runner):
    def __init__(self, base_url="127.0.0.1", verify=False):
        super().__init__(name="Http Runner")
        self.base_url = base_url
        self.http = requests.Session()
        # 登录TOKEN
        self.token = ""