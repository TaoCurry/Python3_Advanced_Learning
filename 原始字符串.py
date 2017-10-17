#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
原始字符串对于反斜线并不会特殊对待，在书写正则表达式的时候，原始字符串会非常有用
不能在原始字符串结尾输入反斜线->原始字符串的最后一个字符不能是反斜线
"""
__author__ = "Curry"
# example
path = 'D:\QQPinyin\\5.6.4103.400\CandOrder'
print(path)
# D:\QQPinyin\5.6.4103.400\CandOrder

# 使用原始字符串，不需要使用转义字符
path = r'D:\QQPinyin\5.6.4103.400\CandOrder'
print(path)
# D:\QQPinyin\5.6.4103.400\CandOrder

# 不能在原始字符串结尾输入反斜线
print(r'This is illegal\')
# missing closing quote
# 对’进行了转义，无法判断字符串在哪里结束

# 最后一个字符串为反斜线的情况
path = r'D:\QQPinyin\5.6.4103.400\CandOrder''\\'
print(path)
# D:\QQPinyin\5.6.4103.400\CandOrder\