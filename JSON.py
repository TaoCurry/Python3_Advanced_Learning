#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
JSON：JavaScript Object Notation, JS 对象标记
JSON表示的对象就是标准的JavaScript语言的对象
JSON标准规定JSON编码是UTF-8

"""
__author__ = "Curry"

# Python -> JSON
import json
d = dict(name='Curry', age=20, score=88)
print(json.dumps(d))   # dumps()方法返回一个str,内容就是标准的JSON

# JSON -> Python
import json
json_str = '{"name": "Curry", "age": 20, "score": 88}'
print(json.loads(json_str))

# JSON进阶

