#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Module(模块) 和包(Package)
__init__.py文件：为了让Python将存储在文件中的模块当作包对待，必须含有一个__init__.py文件。这个文件可以为空，有了这个文件，才可以导入文件目录下的module。
__all__: __init__.py文件中一个重要的变量，以列表的形式显式地展示了模块的公有接口。
"""
__author__ = "Curry"

# 模块是程序，一个.py文件就是一个模块。模块用于定义函数，模块在第一次导入到程序中时被执行，并且拥有自己的作用域。使用模块的好处是方便代码重用，可以在多个程序中使用模块中的代码。

import copy, math

# dir() 模块所有特性（以及模块的函数、类、变量等）以list形式列出
print(dir(
    copy))  # ['Error', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_copy_dispatch', '_copy_immutable', '_deepcopy_atomic', '_deepcopy_dict', '_deepcopy_dispatch', '_deepcopy_list', '_deepcopy_method', '_deepcopy_tuple', '_keep_alive', '_reconstruct', 'copy', 'deepcopy', 'dispatch_table', 'error']
print(dir(
    math))  # ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']

# __all__如何设置了__all__,则导入__all__变量中的成员。如果模块没有设置__all__变量，用from XXX import * 语句默认将会导入模块中所有不以下划线开头的全局名称。例如math模块没有__all__变量，from math import *将没有下划线开头的函数全部一次性导入。copy模块则导入__all__变量已经列出的内容。
print(copy.__all__)  # ['Error', 'copy', 'deepcopy']

# help() 查看模块中某个函数的用法和文档
help(copy.copy)
'''Help on function copy in module copy:

copy(x)
    Shallow copy operation on arbitrary Python objects.
    
    See the module's __doc__ string for more info.
'''
# __doc__ 文档
print(copy.__doc__)

# __file__ 模块源代码的位置
print(copy.__file__)  # C:\Users\xiatao\AppData\Local\Programs\Python\Python36\lib\copy.py
