#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
namedtuple: 具名元组，取值的时候不需要通过下标索引的方式来获取，直接可以字段名获取值
"""
__author__ = "Curry"

from collections import namedtuple


User = namedtuple('User', 'name gender height weight')  # 定义namedtuple类，第一个参数就是元组的名字，第二个参数是用空格隔开的字符串或字符串组成的列表，每个字符串类似与类中的属性.

# 或者
# User = namedtuple('User', ['name', 'gender', 'height', 'weight'])

user = User(name='jack', gender='female', height=170, weight=120)   # 创建一个User对象

print(user.name)
print(user.gender)

'''
namedtuple是继承tuple的一个子类,保留了tuple的特性.namedtuple比tuple的优势在于namedtuple具有自我描述的特点，可以说明各个字段代表什么。
'''
print(user[1:3])    # slicing

# 类似于定义一个User类:
class User:
    def __init__(self, name, gender, height, weight):
        self.name = name
        self.gender = gender
        self.gender = height
        self.weight = weight


user = User(name='Jack', gender='female', height=170, weight=120)
user.name
