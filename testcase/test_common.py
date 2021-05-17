# -*- encoding: utf-8 -*-
"""
@File    : test_common.py
@Time    : 2021/5/17 0017 22:43
@Author  : YuYe
@Email   : kpl1888@163.com
@Software: PyCharm
"""

import pytest
from common.logger import logger
from common.rest_client import RestClient
from common.update_json import update_json
from common.read_file_data import ReadFileData


class TestCommon(object):
    def test_rest_client_json(self):
        pass

    def test_rest_client_data(self):
        pass

    def test_update_json(self):
        pass

    def test_readfile_data(self):
        logger.info("测试读取yaml文件")
        # yaml_data = ReadFileData.load_yaml("config/service.yaml")
        # logger.info("测试读取.ini文件")
        # ini_data = ReadFileData.load_ini("config/setting.ini")
        yaml_data = ReadFileData.load_yaml("data/yaml/access_token.yaml")
        # print(yaml_data)
        l = dict(yaml_data["gettoken"][0])
        for value in l.values():
            print(value)

