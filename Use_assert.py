#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
断言的用法
    断言的定义：编写代码时，我们总是会做出一些假设，断言就是用于在代码中捕捉这些假设，可以将断言看作是异常处理的一种高级形式。断言表示为一些布尔表达式，程序员相信在程序中的某个特定点该表达式值为真。可以在任何时候启用和禁用断言验证，因此可以在测试时启用断言，而在部署时禁用断言。同样，程序投入运行后，最终用户在遇到问题时可以重新起用断言。
"""
__author__ = "Curry"

# example
assert expression1  # Boolean
# is equivalent to
if __debug__:
    if not expression1: raise AssertionError


assert expression1, expression2
# is equivalent to
if __debug__:
    if not expression1: raise AssertionError(expression2)
# 其中Expression1应该总是一个布尔值，Expression2是断言失败时输出的失败消息的字符串。如果Expression1为假，则抛出一个 AssertionError，这是一个错误，而不是一个异常，也就是说是一个不可控制异常（unchecked Exception),AssertionError由于是错误，所以可以不捕获，但不推荐这样做，因为那样会使你的系统进入不稳定状态。

# example
age = 10
assert 0 < age < 10, 'age must between 0 to 10!'
# Traceback (most recent call last):
#  File "<pyshell#5>", line 1, in <module>
#    assert 0 < age < 10, 'age must between 0 - 10'
# AssertionError: age must between 0 - 10