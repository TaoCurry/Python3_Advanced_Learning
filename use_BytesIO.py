#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
BytesIO:在内存中读写字节
"""
__author__ = "Curry"

# example
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))   # 写入的是utf-8编码的中文字节
print(f.getvalue())
# b'\xe4\xb8\xad\xe6\x96\x87'
f.close()