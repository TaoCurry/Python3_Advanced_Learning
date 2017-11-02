#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
相等运算符和is运算符之间的差别
相等运算符主要是判断两个对象是否相等。
IS运算符，也叫做同一性运算符，是用来判断同一性而不是判断相等性,判定两者是否等同（同一个对象）。
"""
__author__ = "Curry"

# example
x = y = [1, 2, 3]
z = [1, 2, 3]

print(x == y)   # True  x, y属于同一个列表对象，值相等
print(x is y)   # True
print(x is z)   # False x, z属于两个不同的列表对象，只是值恰好相等,不具有同一性.
print(x == z)   # True

# example
x = [1, 2, 3]
y = [2, 4]
print(x is not y)
del x[2]
y[1] = 1
y.reverse()
print(x == y)   # True
print(x is y)   # False
