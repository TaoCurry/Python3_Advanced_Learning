#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
deque:高效实现插入和删除操作的双向列表，适合用于队列和栈。
deque方法：
1.append(x)  Add x to the right side of the deque.

2.appendleft(x) Add x to the left side of the deque.

3.clear()  Remove all elements from the deque leaving it with length 0.

4.copy()  Create a shallow copy of the deque.

5.count(x)  Count the number of deque elements equal to x.

6.extend(iterable)  Extend the right side of the deque by appending elements from the iterable argument.

7.extendleft(iterable)  Extend the left side of the deque by appending elements from iterable. Note, the series of left appends results in reversing the order of elements in the iterable argument.

8.pop()  Remove and return an element from the right side of the deque. If no elements are present, raises an IndexError.

9.popleft()  Remove and return an element from the left side of the deque. If no elements are present, raises an IndexError.

10.remove(value)  Remove the first occurrence of value. If not found, raises a ValueError.

11.reverse()  Reverse the elements of the deque in-place and then return None.

12.rotate(n)  Rotate the deque n steps to the right. If n is negative, rotate to the left. Rotating one step to the right is equivalent to: d.appendleft(d.pop()).
"""
__author__ = "Curry"

from collections import deque

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)                # deque(['y', 'a', 'b', 'c', 'x'])
print(q.count('x'))     # 1
q.rotate(2)
print(q)        # deque(['c', 'x', 'y', 'a', 'b'])
q.rotate(-2)
print(q)        # deque(['y', 'a', 'b', 'c', 'x'])