#-*- coding:utf-8 -*-
# @Time : 2020/12/5 20:23 

# @Author : youding

# @File : test_crm_resume.py

# @Software: PyCharm Community Edition

import pytest
from auto.conftest import database_connector
from auto.resources.database_test.conf import CRM_RESUME

def test_crm_resume_has_columns(database_connector):
    db = database_connector
    res = db.has_columns(CRM_RESUME['table_name'], CRM_RESUME['columns'])
    print(res)
    for col in CRM_RESUME['columns']:
        print("exist columns: %s -> %s" %(col, res[col]))
        assert res[col]


def test_crm_resume_primary_key(database_connector):
    db = database_connector
    res = db.is_primary(CRM_RESUME['table_name'], CRM_RESUME['primary'])
    for col in CRM_RESUME['primary']:
        print("exist primary key : %s --> %s" %(col, res[col]))
        assert res[col]



def test_crm_resume_default(database_connector):
    db = database_connector
    res = db.is_default(CRM_RESUME['table_name'], CRM_RESUME['default'])
    for col in CRM_RESUME['default']:
        print("exist default: %s --> %s" %(col, res[col]))
        assert res[col]


def test_crm_resume_index(database_connector):
    db = database_connector
    # res = db.is_unique(CRM_RESUME['table_name'], CRM_RESUME['unique'])
    res = db.is_index(CRM_RESUME['table_name'], CRM_RESUME['index'])
    # print(res)
    for col in CRM_RESUME['index']:
        print("exist index: %s --> %s" %(col, res[col]))
        assert res[col]


