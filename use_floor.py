#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
math模块floor()方法
math.floor()
Return the floor of x, the largest integer less than or equal to x. If x is not a float, delegates to x.__floor__(), which should return an Integral value.
返回数字的下舍整数
"""
__author__ = "Curry"

# example
import math
print('math.floor(-45.17) is:', math.floor(-45.17))
# math.floor(-45.17) is: -46
print('math.floor(32.9) is:', math.floor(32.9))
# math.floor(32.9) is: 32