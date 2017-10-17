#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Pickle标准模块，通过它可以将任何纯文本对象存储到一个文件中，并在稍后将其取回。
Pickle可以实现序列化。
序列化 pickling：变量从内存中变成可存储或传输的过程。比如可以写入磁盘、进行网络传输等
反序列化 unpickling：把变量内容从序列化的对象重新读到内存里
"""
__author__ = "Curry"
# example
import  pickle
# 需要存储的文本对象名字
shopfile = 'shoplist.data'

shoplist = ['Iphone', 'MacBookPro', 'Ipad']
f= open(shopfile, 'wb')
# 将文本对象存储到这个文件中
pickle.dump(shoplist, f)


# example
import pickle
d = dict(name='Curry', age=23, height=6)
print(pickle.dumps(d))
# b'\x80\x03}q\x00(X\x04\x00\x00\x00nameq\x01X\x05\x00\x00\x00Curryq\x02X\x03\x00\x00\x00ageq\x03K\x17X\x06\x00\x00\x00heightq\x04K\x06u.'
f = open('D:\Python3_Advanced\dump.txt', 'wb')
pickle.dump(d, f)
f.close()

f = open('D:\Python3_Advanced\dump.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)
# {'name': 'Curry', 'age': 23, 'height': 6}