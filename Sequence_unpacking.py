#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
序列解包/递归解包
解包的序列中的元素必须和放置在赋值符号=左边的变量的数量完全一致，否则Python会在赋值时引发异常
"""
__author__ = "Curry"

x, y, z = 1, 2, 3
print(x, y, z)
# 1, 2, 3

x, y = y, x
print(x, y, z)
# 2, 1, 3

d = {'name': 'Curry', 'age': 28}
a, b = d.popitem()
print(a, b)
# age 28