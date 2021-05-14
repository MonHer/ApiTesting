# -*- encoding: utf-8 -*-
"""
@File    : rest_client.py
@Time    : 2021/5/15 0015 0:52
@Author  : YuYe
@Email   : kpl1888@163.com
@Software: PyCharm
"""

import requests


class RestClient(object):

    def client(self, url, method, headers, json, **kwargs):
        self.client = requests.request(url=url, method=method, headers=headers, json=json, **kwargs)
        return self.client.json()
