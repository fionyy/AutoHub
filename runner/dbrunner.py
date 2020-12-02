# -*- coding: utf-8 -*-
# @Time : 2020/11/30 19:24 

# @Author : youding

# @File : dbrunner.py

# @Software: PyCharm Community Edition

from sqlalchemy import create_engine
from sqlalchemy.engine import reflection
from sqlalchemy.dialects.mysql import *
from .baserunner import BaseRunner




class DbRunner(BaseRunner):
    def __init__(self, conn_str="", encoding="utf-8", echo=False):
        super().__init__(name="Database Runner")

        engine = create_engine(conn_str, encoding=encoding, echo=echo)

        self.insp = reflection.Inspector.from_engine(engine)

    def has_tables(self, tabels_name=[]):
        res = {}
        tables = self.insp.get_table_names()
        # print(tables)
        for table in tabels_name:
            if table in tables:
                res[table] = True
            else:
                res[table] = False
        return res

    def has_columns(self, table_name, columns_name=[]):

        res = {}
        for col in columns_name:
            res[col] = self.__find_column(table_name, col) != None
        return res

    def is_default(self, table_name, columns=[]):
        '''
        判断是否有默认值
        :param table_name:
        :param columns: 字段 是否默认 以字典形式 存储在列表中
        :return:
        '''
        res = {}
        for col in columns:
            # 字段及默认值的键值对
            k, v = col.popitem()
            # print(k, v)
            de = self.__find_column(table_name, k)
            # print(de['default'])
            # print(v)
            if de['default'] == str(v):
                res[k] = True
            else:
                res[k] = False
        return res

    def is_primary(self, table_name, columns_name=[]):
        '''
        是否主键
        :param table_name:
        :param columns_name:
        :return:
        '''
        res = {}
        primary = self.insp.get_pk_constraint(table_name)
        for col in columns_name:
            if col in primary['constrained_columns']:
                res[col] = True
            else:
                res[col] = False
        return res

    def is_unique(self, table_name, columns_name=[]):
        '''
        返回是否唯一键
        :param table_name:
        :param columns_name:
        :return:
        '''
        res = {}
        # 获取unique 字段 列表
        unique = self.insp.get_unique_constraints(table_name)
        # print(unique)
        for col in columns_name:
            res[col] = False
            for i in unique:
                if col in i['column_names']:
                    res[col] = True

        return res

    def is_nullable(self, table_name, columns_name=[]):
        res = {}
        for col in columns_name:
            nullable = self.__find_column(table_name, col)
            res[col] = nullable['nullable']
        return res


    def is_index(self, table_name, columns_name=[]):
        res = {}
        indexs = self.insp.get_indexes(table_name)
        for col in columns_name:
            res[col] = False
            for name in indexs:
                # print(name)
                if col == name['column_names'][0]:
                    # print(col, name['column_names'][0])
                    res[col] = True

        return res


    def __find_column(self, table_name, column_name):
        # 每个字段一个字典
        columns = self.insp.get_columns(table_name)
        # print(columns)
        for col in columns:
            if column_name == col["name"]:
              return col

        return None

