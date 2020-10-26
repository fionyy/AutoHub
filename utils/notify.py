# -*- coding: utf-8 -*-
# @Time : 2020/10/26 15:41 

# @Author : youding

# @File : notify.py

# @Software: PyCharm Community Edition


import json

import requests

from conf.conf import DINGTALK_URL


def send_dingtalk_msg(msg):
    headers = {"Content-Type": "application/json"}
    data = {
        "msgtype": "text",
        "text": {
            "content": msg
        }
    }

    res = requests.post(DINGTALK_URL, data=json.dumps(data), headers=headers)
    print(res.text)


# send_dingtalk_msg('hello')