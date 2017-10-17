#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
math模块ceil()方法
Return the ceiling of x, the smallest integer greater than or equal to x. If x is not a float, delegates to x.__ceil__(), which should return an Integral value.
返回数字上入整数
"""
__author__ = "Curry"

# example
import math
print('math.ceil(4.1) is:', math.ceil(4.1))
# math.ceil(4.1) is: 5
print('math.ceil(-3.2) is:', math.ceil(-3.2))
# math.ceil(-3.2) is: -3