#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
    translate()方法和replace()方法一样，可以替换字符串中的某些部分，translate方法只处理单个字符。
它的优势在于可以同时进行多个替换，有些时候比replace方法效率高。
    在使用translate转换之前，需要先指定一张转换表，这里使用str.maketrans()方法进行转换.
    static str.maketrans(x[, y[, z]])
    This static method returns a translation table usable for str.translate(). <为str.transl()提供转换表>
If there is only one argument, it must be a dictionary mapping Unicode ordinals (integers) or characters (strings of length 1) to Unicode ordinals, strings (of arbitrary lengths) or None. Character keys will then be converted to ordinals.
If there are two arguments, they must be strings of equal length, and in the resulting dictionary, each character in x will be mapped to the character at the same position in y. If there is a third argument, it must be a string, whose characters will be mapped to None in the result.
    static str.maketrans(x, y, z)静态方法， x, y前两个参数表示将x中的字符串用y替代，如果存在第三个参数，这个z参数必须是应该string，同时删除它。
"""
__author__ = "Curry"
import  string
x = 'Hello!LOL!'
a = str.maketrans('', '', string.punctuation)   # reduce a table for str.translate()
x = x.translate(a)
# string.capwords(s, seq);
print(x)    # HelloLoL
