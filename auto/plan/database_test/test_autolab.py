# -*- coding: utf-8 -*-
# @Time : 2020/11/9 22:29 

# @Author : youding

# @File : test_autolab.py

# @Software: PyCharm Community Edition

import pytest
from runner.runner import DbRunner
from auto.conftest import database_connector
from auto.resources.database_test.conf import RANZHI

def test_ranzhi_tables(database_connector):
    db = database_connector
    res = db.has_tables(RANZHI['tables'])
    for table in RANZHI['tables']:
        print('table %s in database' %table)
        assert res[table]