# -*- encoding: utf-8 -*-
"""
@File    : rest_client.py
@Time    : 2021/5/15 0015 0:52
@Author  : YuYe
@Email   : kpl1888@163.com
@Software: PyCharm
"""

import requests
from common.logger import logger


class RestClient(object):
    @staticmethod
    def client_json(url, method, headers, json, **kwargs):
        client = requests.request(url=url, method=method, headers=headers, json=json, **kwargs)
        logger.info(client.json())
        return client

    @staticmethod
    def client_data(url, method, headers, data, **kwargs):
        client = requests.request(url=url, method=method, headers=headers, data=data, **kwargs)
        logger.info(client.json())
        return client
