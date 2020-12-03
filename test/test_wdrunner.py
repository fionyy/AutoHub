# -*- coding: utf-8 -*-
# @Time : 2020/12/1 16:24 

# @Author : youding

# @File : test_wdrunner.py

# @Software: PyCharm Community Edition


import sys
import os
from unittest import runner
cur_path = os.path.abspath(os.path.dirname(__file__))
root_path = os.path.split(cur_path)[0]
sys.path.append(root_path)
bin_path = root_path + '\\bin'
sys.path.append(bin_path)
# print(sys.path)
# sys.path.append(root_path + '\\bin')

import unittest
from runner.runner import WbRunner

class TestWdrunner(unittest.TestCase):
    runner = WbRunner()
    # c_path = cur_path = os.path.abspath(os.path.dirname(__file__))
    # print(c_path)

    wd = runner.chrome_driver(executable_path=root_path + ".\\bin\\chromedriver.exe")
    wd.get('http://www.baidu.com')
    wd.close()



if __name__ == '__main__':
    unittest.main()