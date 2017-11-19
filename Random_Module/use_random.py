#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
random模块包含返回随机数的函数，可以用于模拟或者任何产生随机输出的程序。实际上所产生的随机数字都是伪随机数，看起来是完全随机的，实际上是以一个可预测的系统作为基础。
random模块中函数:
floating:
random.random(): Return the next random floating point number in the range [0.0, 1.0). 返回0.0-1.0的随机浮点数
random.uniform(a, b): Return a random floating point number N such that a <= N <= b for a <= b and b <= N <= a for b < a. 返回a-b之间的随机浮点数.

integer:
random.randrange(start, stop[, step]): 返回range()中的随机数，步长可以选择.
random.randint(a, b): Return a random integer N such that a <= N <= b.

sequence:
random.choice(seq): Return a random element from the non-empty sequence seq. 从非空序列中返回一个随机元素。
random.choices(population, weights=None, *, cum_weights=None, k=1): 从序列中返回一个k大小的子序列。
random.shuffle(x[, random]): Shuffle the sequence x in place. 将序列中的元素打乱，会改变原序列。
random.sample(population, k):Return a k length list of unique elements chosen from the population sequence or set. Used for random sampling without replacement. 从序列中选择k个随机并且独立的元素，元素互不相同。

bits:
random.getrandbits(k): Returns a Python integer with k random bits.

"""
__author__ = "Curry"

import random

print(random.random())  # 0-1之间的浮点数
print(random.uniform(0, 10))  # 0-10之间的浮点数
print(random.uniform(12, 1))
print(random.randrange(10))  # 0-9之间的整数
print(random.randrange(0, 10, 2))  # 0-9之间的偶数
print(random.randint(0, 10))  # 0-10之间的整数
print(random.choice(list('XYZ')))  #
# print(random.choice([]))    # 空序列抛出一个IndexError('Cannot choose from an empty sequence') from None
print(random.choices([1, 2, 3, 4], k=2))  # [x, x]
lst = [1, 2, 3, 4]
random.shuffle(lst)  #
print(lst)
print(random.sample([1, 2, 2, 3, 4], k=2))
print(random.getrandbits(2))