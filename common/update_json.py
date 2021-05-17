# -*- encoding: utf-8 -*-
"""
@File    : update_json.py
@Time    : 2021/5/17 0017 22:26
@Author  : YuYe
@Email   : kpl1888@163.com
@Software: PyCharm
"""


def update_json(mydict, key, value):
    if isinstance(mydict, dict):  # 使用isinstance检测数据类型，如果是字典
        if key in mydict.keys():  # 替换字典第一层中所有key与传参一致的key
            mydict[key] = value
        for k in mydict.keys():  # 遍历字典的所有子层级，将子层级赋值为变量chdict，分别替换子层级第一层中所有key对应的value，最后在把替换后的子层级赋值给当前处理的key
            chdict = mydict[k]
            update_json(chdict, key, value)
            mydict[k] = chdict
    elif isinstance(mydict, list):  # 如是list
        for element in mydict:  # 遍历list元素，以下重复上面的操作
            if isinstance(element, dict):
                if key in element.keys():
                    element[key] = value
                for k in element.keys():
                    chdict = element[k]
                    update_json(chdict, key, value)
                    element[k] = chdict
