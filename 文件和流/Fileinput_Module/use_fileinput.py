#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
fileinput — Iterate over lines from multiple input streams.迭代来自多个输入流的行数。
fileinput模块中重要的函数：
1.fileinput.input(files=None, inplace=False, backup='', bufsize=0, mode='r', openhook=None) --> files:文件名; inplace:是否将标准输出的结果写回文件，默认否; backup:备份文件扩展名; mode:读写模式，默认为读; bufsize:缓冲区大小.
2.fileinput.filename() -->Return the name of the file currently being read. Before the first line has been read, returns None.
3.fileinput.flineno() -->Return the integer “file descriptor” for the current file. When no file is opened (before the first line and between files), returns -1. 返回当前文件的行数
4.fileinput.lineno() -->Return the cumulative line number of the line that has just been read. Before the first line has been read, returns 0. After the last line of the last file has been read, returns the line number of that line.返回当前累计的行数
5.fileinput.isfirstline() -->
6.fileinput.isstdin() --> 检查最后一行是否来自sys.stdin
7.fileinput.nextfile() --> 关闭当前文件，移动到下个文件
8.fileinput.close() --> 关闭序列
"""
__author__ = "Curry"

import fileinput

# 最常见的操作，读取文件中的每一行
for line in fileinput.input(r'C:\Users\xiatao\Desktop\Test.txt'):
    print(line)