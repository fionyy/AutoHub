# -*- coding: utf-8 -*-
# @Time : 2020/11/9 22:30 

# @Author : youding

# @File : conf.py

# @Software: PyCharm Community Edition
CRM = {
    'conn_str': 'mysql+pymysql://root:ayou0630@192.168.106.20:3306/ranzhi?charset=utf8',
    'encoding': 'utf-8',
    'echo': False,
    'tables': ['crm_address', 'crm_contact', 'crm_delivery', 'crm_plan', 'crm_contract'],
}

CRM_ADDRESS = {
    'table_name': 'crm_address',
    'columns': ['id', 'objectType', 'objectID', 'title', 'area', 'location'],
    'primary': ['id'],
    'index': ['objectType']
}

CRM_RESUME = {
    'table_name': 'crm_resume',
    'columns': ['id', 'contact', 'customer', 'maker', 'dept', 'title', 'address', 'join', 'left', 'deleted'],
    'default': {"maker":"'0'", "deleted":"'0'"},
    'index': ['contact', 'customer', 'left', 'maker'],
    'primary': ['id']
}