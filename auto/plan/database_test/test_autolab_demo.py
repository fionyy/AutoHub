# -*- coding: UTF-8 -*-
# @Time : 2020/11/9 22:29 

# @Author : youding

# @File : test_autolab_demo.py

# @Software: PyCharm Community Edition

import pytest
from auto.conftest import database_connector
from runner.runner import DbRunner
from auto.resources.database_test.conf import CRM_ADDRESS

def test_crm_address_columns_exist(database_connector):
    db = database_connector
    res = db.has_columns(CRM_ADDRESS['table_name'], CRM_ADDRESS['columns'])
    print(res)
    for column in CRM_ADDRESS['columns']:
        print("exist column: %s --> %s"%(column, res[column]))
        assert res[column]



def test_crm_address_primary_key(database_connector):
    db = database_connector
    res = db.is_primary(CRM_ADDRESS['table_name'], CRM_ADDRESS['primary'])
    for col in CRM_ADDRESS['primary']:
        print('exist primary key: %s --> %s' %(col, res[col]))
        assert res[col]


def test_crm_address_index(database_connector):
    db = database_connector
    res = db.is_index(CRM_ADDRESS['table_name'], CRM_ADDRESS['index'])
    for col in CRM_ADDRESS['index']:
        print("exist index: %s --> %s"%(col, res[col]))
        assert res[col]