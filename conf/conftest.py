# -*- coding: utf-8 -*-
# @Time : 2020/10/26 15:17 

# @Author : youding

# @File : conftest.py

# @Software: PyCharm Community Edition

import pytest
import platform
from utils.notify import send_dingtalk_msg


@pytest.fixture
def data_cache(request):
    return request.config.cache

def pytest_sessionstart(session):
    session.results = dict()


def pytest_sessionfinish(session, existatus):
    failed_count = sum(1 for result in session.results.vaules() if result.failed)
    if failed_count != 0:
        report_content = 'Failed Notify'
        index = 1
        for result in session.results.values():
            report_content += "%d. %s \n" %(index, result.location[2])
            index = index + 1

        send_dingtalk_msg(report_content)
