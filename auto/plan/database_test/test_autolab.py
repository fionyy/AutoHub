# -*- coding: UTF-8 -*-
# @Time : 2020/11/9 22:29 

# @Author : youding

# @File : test_autolab.py

# @Software: PyCharm Community Edition

import pytest
from runner.runner import DbRunner
from auto.conftest import database_connector
from auto.resources.database_test.conf import CRM

def test_ranzhi_tables(database_connector):
    db = database_connector
    res = db.has_tables(CRM['tables'])
    for table in CRM['tables']:
        print('table %s in database' %table)
        assert res[table]