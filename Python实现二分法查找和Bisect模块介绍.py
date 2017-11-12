#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
二分查找又称折半查找，优点是比较次数少，查找速度快，平均性能好，占用系统内存较少；其缺点是要求待查表为有序表，且插入删除困难。因此，折半查找方法适用于不经常变动而查找频繁的有序列表。
bisect：cut in half, halve, divide/cut/split in two, split down the middle, cross,intersect.英文解释为对分。
"""
__author__ = "Curry"


def binary_search_recursion(sequence, number, lower, upper):
    ''' 构造一个递归实现二分法查找序列的函数

    :param sequence: 传入一个序列，并且是已经排序过的
    :param number: 假设需要查找的序列中的元素
    :param lower: 已经排序完成后的序列的下限
    :param upper: 排序过后序列的上限
    '''
    if lower == upper:
        assert number == sequence[upper]  # 如果序列上下限相等，取上限的值
        return upper

    else:
        middle = (lower + upper) // 2  # 取上下限的平均值
    if number > middle:  # 需要查找的数字大于平均值
        return binary_search_recursion(sequence, number, middle + 1, upper)
    else:
        return binary_search_recursion(sequence, number, lower, middle)


def binary_search_loop(sequence, number, lower, upper):
    '''使用循环来实现二分法查找

    :param sequence:
    :param number:
    :param lower:
    :param upper:
    :return:
    '''
    while lower <= upper:
        middle = (lower + upper) // 2
        if sequence[middle] < number:
            lower = middle + 1
        elif sequence[middle] > number:
            upper = middle - 1
        else:
            return middle


def binary_search_bisect(sequence, number):
    from bisect import bisect_left
    i = bisect_left(sequence, number)
    if i != len(sequence) and sequence[i] == number:
        return i


# 进行性能测试，比较递归和循环实现二分法查找的效率
if __name__ == '__main__':
    import timeit

    seq = list(range(10000))
    seq.sort()


    def test_recursion():
        binary_search_recursion(seq, 99, 0, len(seq) - 1)


    def test_loop():
        binary_search_loop(seq, 99, 0, len(seq) - 1)

    def test_bisect():
        binary_search_bisect(seq, 99)


    t1 = timeit.Timer('test_recursion()', setup='from __main__ import test_recursion')
    t2 = timeit.Timer('test_loop()', setup='from __main__ import test_loop')
    t3 = timeit.Timer('test_bisect()', setup='from __main__ import test_bisect')

    print('Recursion:', t1.timeit())    # Recursion: 7.891379073228306
    print('Loop:', t2.timeit())     # Loop: 5.48589972802381  可见循环效率高于递归
    print('Bisect:', t3.timeit())   # Bisect: 3.0437822137835493 使用bisect模块效率更快
'''
    Python 有一个 bisect 模块，用于维护有序列表。bisect 模块实现了一个算法用于插入元素到有序列表。在一些情况下，这比反复排序列表或构造一个大的列表再排序的效率更高。Bisect 是二分法的意思，这里使用二分法来排序，它会将一个元素插入到一个有序列表的合适位置，这使得不需要每次调用 sort 的方式维护有序列表。
'''
"""
Bisect模块提供的函数有：
1. bisect.bisect_left(a,x, lo=0, hi=len(a)) : 查找在有序列表 a 中插入 x 的index。lo 和 hi 用于指定列表的区间，默认是使用整个列表。如果 x 已经存在，在其左边插入。返回值为 index

2. bisect.bisect_right(a,x, lo=0, hi=len(a)) & bisect.bisect(a, x, lo=0, hi=len(a)) ：右边插入

3. bisect.insort_left(a,x, lo=0, hi=len(a)) ：在有序列表 a 中插入 x。和 a.insert(bisect.bisect_left(a,x, lo, hi), x) 的效果相同。

4. bisect.insort_right(a,x, lo=0, hi=len(a))

bisect* 只用于查找 index， 不进行实际的插入；而 insort* 则用于实际插入。
"""

# example

import bisect
import random

random.seed(1)  # 产生一个随机数种子
print('New Pos Contents')
print('--- --- --------')
lst = []
for i in range(1, 15):
    r = random.randint(1, 100)  # 生成一个随机整数
    position = bisect.bisect(lst, r)  # 找到刚刚生成的随机整数的index
    bisect.insort(lst, r)  # 将这个随机数插入到序列的index中
    print('%3d %3d' % (r, position), lst)

New Pos Contents
--- --- --------
 18   0 [18]
 73   1 [18, 73]
 98   2 [18, 73, 98]
  9   0 [9, 18, 73, 98]
 33   2 [9, 18, 33, 73, 98]
 16   1 [9, 16, 18, 33, 73, 98]
 64   4 [9, 16, 18, 33, 64, 73, 98]
 98   7 [9, 16, 18, 33, 64, 73, 98, 98]
 58   4 [9, 16, 18, 33, 58, 64, 73, 98, 98]
 61   5 [9, 16, 18, 33, 58, 61, 64, 73, 98, 98]
 84   8 [9, 16, 18, 33, 58, 61, 64, 73, 84, 98, 98]
 49   4 [9, 16, 18, 33, 49, 58, 61, 64, 73, 84, 98, 98]
 27   3 [9, 16, 18, 27, 33, 49, 58, 61, 64, 73, 84, 98, 98]
 13   1 [9, 13, 16, 18, 27, 33, 49, 58, 61, 64, 73, 84, 98, 98]


def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)  # 返回对应分数段对应的成绩的索引值
    return grades[i]


print([grade(score) for score in [33, 99, 70, 89, 90, 100]])    # ['F', 'A', 'C', 'B', 'A', 'A']
print(grade(10))    # F

