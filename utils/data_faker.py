# -*- coding: utf-8 -*-
# @Time : 2020/12/1 15:27 

# @Author : youding

# @File : data_faker.py

# @Software: PyCharm Community Edition

from faker import Faker
from faker.providers import BaseProvider

import  string

localized = True

class DateFaker(BaseProvider):

    def __init__(self):
        self.faker = Faker()