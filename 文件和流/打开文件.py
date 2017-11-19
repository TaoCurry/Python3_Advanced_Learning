#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)打开文件函数，返回一个文件对象。

file:文件名，必选参数，包含文件的位置和格式。

mode: 打开文件的模式。'r'：默认读取文件；'w':写入文件；'x': ; 'a': 写入文件模式，并在末尾自动追加写入内容；'t': txt文本模式打开（默认）; 'b': 二进制模式打开; 'U': 通用换行符支持；‘+’: 可读写模式。

buffering：可选参数，控制文件的缓冲。如果buffering=0\False,I\O就是无缓存的（所有的读写都直接针对硬盘）。如果buffering = 1,I\O就是有缓冲的（使用内存来代替硬盘，让程序更快），大于1的数字代表缓冲区的大小（单位是字节），-1或者是任意负数代表默认使用缓冲区大小。


"""
__author__ = "Curry"