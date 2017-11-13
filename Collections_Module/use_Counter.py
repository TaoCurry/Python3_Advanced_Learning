#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Counter:dict subclass for counting hashable objects.dict的一个子类.
"""
__author__ = "Curry"

from collections import Counter

c = Counter()
for ch in 'Programming':
    c[ch] += 1

print(c)  # Counter({'r': 2, 'g': 2, 'm': 2, 'P': 1, 'o': 1, 'a': 1, 'i': 1, 'n': 1})
