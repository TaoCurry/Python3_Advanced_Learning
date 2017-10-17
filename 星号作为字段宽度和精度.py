#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
使用指定宽度打印格式化后的价格表
1
"""
__author__ = "Curry"

# example
width = int(input('please enter width: '))
price_width = 10
item_width = width - price_width
header_format = '%-*s%*s'       # 使用*作为字段精度，需要从tuple中读出
_format = '%-*s%*.2f'       #
print('=' * width)
print(header_format % (item_width, 'Item', price_width, 'Price'))   # 建立一个tuple类型
print('-' * width)
print(_format % (item_width, 'Apple', price_width, 0.4))
print(_format % (item_width, 'Pears', price_width, 0.5))
print(_format % (item_width, 'Orange', price_width, 9.999))
print('=' * width)



 please enter width: 35
 ===================================
 Item                          Price
 -----------------------------------
 Apple                          0.40
 Pears                          0.50
 Orange                        10.00
 ===================================
11