#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
DocStrings：文档字符串可以更好的记录程序并让程序更好的理解。
"""
__author__ = "Curry"

# example
def print_max(x, y):
    '''

    :param x:
    :param y:
    '''
    x = int(x)
    y = int(y)
    if x > y:
        print(x)
    else:
        print(y)
print_max(3, 5)
print(print_max.__doc__)
print(__author__)