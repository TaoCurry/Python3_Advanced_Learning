#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
调用堆栈分析错误&&记录错误&&抛出错误
"""
__author__ = "Curry"

import logging  # 使用logging模块记录错误，程序会执行再退出，错误会被记录下来


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)


main()
print('END')

END
ERROR:root:division by zero
Traceback (most recent call last):
  File "D:/Python3进阶学习/Python3_Advanced_Learning/错误处理.py", line 22, in main
    bar('0')
  File "D:/Python3进阶学习/Python3_Advanced_Learning/错误处理.py", line 17, in bar
    return foo(s) * 2
  File "D:/Python3进阶学习/Python3_Advanced_Learning/错误处理.py", line 13, in foo
    return 10 / int(s)
ZeroDivisionError: division by zero

    
def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n


def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise   # raise语句如果不带参数，就会把当前错误原样抛出。

        
bar()

Traceback (most recent call last):
ValueError!
  File "D:/Python3进阶学习/Python3_Advanced_Learning/错误处理.py", line 24, in <module>
    bar()
  File "D:/Python3进阶学习/Python3_Advanced_Learning/错误处理.py", line 18, in bar
    foo('0')
  File "D:/Python3进阶学习/Python3_Advanced_Learning/错误处理.py", line 12, in foo
    raise ValueError('invalid value: %s' % s)
ValueError: invalid value: 0

