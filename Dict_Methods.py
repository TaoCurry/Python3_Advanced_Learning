#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
字典方法的详细说明
"""
__author__ = "Curry"
#  clear()方法 --dict.clear() 清楚字典中的所有项
# 该函数没有返回值，属于原地操作
# example 1
d = dict([('name', 'Curry'), ('gae', 20)])
d1 = d.clear()
print(d)    # {}
print(d1)   # None

# example 2
x = {}
y = x
x['key'] = 'value'
print(y)    # {'key': 'value'}
print(x)    # {'key': 'value'}
x = {}
print(x)    # {}
print(y)    # {'key': 'value'}

# example 3
x = {}
y = x
x['key'] = 'value'
print(y)    # {'key': 'value'}
x.clear()
print(y)    # {}



