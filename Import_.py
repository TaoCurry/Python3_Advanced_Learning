#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
从模块导入函数的几种方式
"""
__author__ = "Curry"


import somemodule   # 导入某个模块
somemodule.somefunction.xxx()

from somemodule import somefunction, anotherfunction    # 从某个模块中导入特定函数功能
somefunction.xxx()

from somemodule import *    # 导入某个模块中的全部功能

import math as Math    # 导入某个模块，并用as后的名称替代这个模块名
Math.floor()

from math import sqrt as LOL    # 从某个模块中导入某个函数，并用as语句后的名称替代该函数名