#!/usr/bin/env python
# coding: utf-8

# @Time    : 2019/4/9 15:35
# @Author  : Yuang
# @Email   : catyuang@gmail.com
# @File    : time_this.py
# @Software: PyCharm
# @Function: 时长装饰器


import time
from functools import wraps


def time_this(func):
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return res
    
    return wrapper
