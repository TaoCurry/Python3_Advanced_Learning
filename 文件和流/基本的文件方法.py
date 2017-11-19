#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
读写文件、关闭文件。
"""
__author__ = "Curry"

# 迭代读取文件中的每一个字符。
with open(r'C:\Users\xiatao\Desktop\Test1.txt', 'r') as file:
    while True:
        char = file.read(1)
        if not char:
            break
        print('String: ', char)

# 迭代读取文件中的每一行。
with open(r'C:\Users\xiatao\Desktop\Test.txt', 'r') as file:
    while True:
        line = file.readline()    # file.readlines() 返回的是一个序列，如果文件很大会占用很多内存。
        if not line:
            break
        print(line)


# 文件非常大，使用fileinput实现懒惰行迭代
import fileinput

for line in fileinput.input(r'C:\Users\xiatao\Desktop\Test.txt'):   # fileinput.input()类似readlines()方法
    print(line)
