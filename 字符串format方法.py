#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""

"""
__author__ = "Curry"
# example1
age = 20
name = 'Curry'
print('{0} was {1} years old'.format(name, age))
print('{} was {} years old'.format(name, age))

# example2
print('{0:.3f}'.format(1.0/3))
# 0.333
print('{0:^11}'.format('Curry'))
#    Curry
print('{0:_^11}'.format('Curry'))
# ___Curry___
print('{name} read the {book}'.format(name='I', book='Python3'))
# I read the Python3
print('a', end='')
print('b', end='')
# ab