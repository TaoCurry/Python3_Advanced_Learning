
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
pow()内置BIF和math模块pow()方法的区别
"""
__author__ = "Curry"

# pow() BIF
print('pow(100,2) is:', pow(100, 2))
# 10000 int型

# math.pow()
import math
print('math.pow(100, 2) is:', math.pow(100, 2))
# 10000.0 返回为float型
