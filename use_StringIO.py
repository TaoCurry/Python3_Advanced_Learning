#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
StringIO:在内存中读写str
"""
__author__ = "Curry"

# example
from io import StringIO
f = StringIO()
f.write('Hello')
# 5
f.write(' ')
# 1
f.write('World!')
# 6
print(f.getvalue())
# getvalue()方法用于获取写入后的str

# 读取StringIO
from io import StringIO
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

