#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
序列
序列的主要功能:
资格测试：in  & not in
索引操作：index，它们能够允许我们获取序列中的特定项目
序列的三种形态：列表；元组；字符串
创建序列副本：使用切片slice操作，切片会产生两个对象。而不是简单的变量赋值，变量只会指向同一个对象，内存地址相同。
Python包含6种内建的序列：
list/tuple/strings/Unicode/buffer/range(xrange 老版本）
所有的序列都可以进行某些特定的操作：
indexing/slicing/adding/multiplying/iteration
"""
__author__ = "Curry"
# example
'''
切片产生两个对象。
使用内置函数id()
id(obj, /)
    Return the identity of an object.
    
    This is guaranteed to be unique among simultaneously existing objects.
    (CPython uses the object's memory address.)
'''
l = list(range(0, 6))
print(id(l))
# 1821737633288
x = l
print(id(x))
# 1821737633288
x = l[:]
print(id(x))
# 2072711707528 内存地址不同
