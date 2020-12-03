# -*- coding: utf-8 -*-
# @Time : 2020/12/1 15:55 

# @Author : youding

# @File : test_dbrunner.py

# @Software: PyCharm Community Edition

import sys
import os
# from unittest import runner
cur_path = os.path.abspath(os.path.dirname(__file__))
root_path = os.path.split(cur_path)[0]
sys.path.append(root_path)

import unittest
from runner.runner import DbRunner

class TestDbrunner(unittest.TestCase):
    conn = "mysql+pymysql://root:ayou0630@192.168.106.20:3306/ranzhi?charset=utf8"
    table_name = 'crm_address'
    def test_has_columns(self):
        runner = DbRunner(self.conn)
        columns = ['id', 'objectType', 'objectID', 'title', 'area','location']
        res = runner.has_columns(self.table_name, columns)
        for col in columns:
            print("has column: %s -> %s" % (col, res[col]))
            assert res[col] == True


if __name__ == '__main__':
    unittest.main()