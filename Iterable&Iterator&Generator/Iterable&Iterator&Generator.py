#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
理解Python 迭代对象、迭代器、生成器
"""
__author__ = "Curry"

# 容器: 是一种把多个元素组织在一起的数据结构，容器中的元素可以逐个地迭代获取，可以用 in, not in关键字判断元素是否包含在容器中。
# 常见的容器对象有： list/deque/set/frozenset/dict/defaultdict/OrderedDict/Counter/tuple/namedtuple/str

# 可迭代对象(Iterable): 能够实现iter()方法的容器。

# 迭代器(Iterator): 是一个带状态的对象，他能在你调用 next()方法的时候返回容器中的下一个值，任何实现了 __next__()方法的对象都是迭代器。以一种延迟计算(lazy evaluation)方式返回元素。

# 生成器(Generator): 一种特殊的迭代器，拥有yield关键字或者生成器表达式。