# _*_ coding: utf-8 _*_
# @Time : 2020/12/1 16:17 

# @Author : youding

# @File : test_httprunner.py

# @Software: PyCharm Community Edition

import sys
import os
from unittest import runner
cur_path = os.path.abspath(os.path.dirname(__file__))
root_path = os.path.split(cur_path)[0]
sys.path.append(root_path)

import unittest
from runner.runner import HttpRunner

class TestHttprunner(unittest.TestCase):
    runner = HttpRunner('http://www.baidu.com')
    r = runner.request('GET', '/')


    encoding = runner.encoding
    print(encoding)

    status_code = runner.status_code
    assert status_code == 200


if __name__ == '__main__':
    unittest.main()