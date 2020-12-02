# -*- coding: utf-8 -*-
# @Time : 2020/11/9 22:29 

# @Author : youding

# @File : test_autolab_demo.py

# @Software: PyCharm Community Edition

import pytest
from auto.conftest import database_connector

from runner.runner import DbRunner
from auto.resources.database_test.conf import RANZHI_CRM_ADDRESS

def test_crm_address_columns_exist(database_connector):
    db = database_connector
    res = db.has_columns(RANZHI_CRM_ADDRESS['columns'])
    print(res)
    for column in RANZHI_CRM_ADDRESS['columns']:
        print("exist column: %s --> %s"%(column, res[column]))
        assert res[column]



def test_crm_address_primary_key(database_connector):
    db = database_connector
    res = db.is_primary_key(RANZHI_CRM_ADDRESS['table_name'], RANZHI_CRM_ADDRESS['primary'])
    for col in RANZHI_CRM_ADDRESS['primary']:
        print('exist primary key: %s --> %s' %(col, res[col]))
        assert res[col]




if __name__ == '__main__':
    # db = database_connector()
    # result = test_crm_address_columns_exist(db)
    # # print(res)

    pass