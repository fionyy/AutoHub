# -*- coding: utf-8 -*-
# @Time : 2020/10/26 15:17

# @Author : youding

# @File : conftest.py

# @Software: PyCharm Community Edition

import pytest
from .resources.database_test.conf import CRM
from runner.runner import DbRunner

@pytest.fixture
def database_connector():
    return DbRunner(conn_str=CRM['conn_str'])


@pytest.fixture
def datatest_connector():
    pass


@pytest.fixture
def http_connector():
    pass


@pytest.fixture
def web_socket_connector():
    pass


@pytest.fixture
def tcp_connector():
    pass


@pytest.fixture
def udp_connector():
    pass

@pytest.fixture
def web_connector():
    """
    return selenium webdriber object
    :return:
    """