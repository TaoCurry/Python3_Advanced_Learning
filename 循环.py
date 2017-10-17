#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#计算1+2+3+4+5+...+100
sum = 0
n = 1
while n <= 100:
	sum = n + sum
	n = n + 1
print(sum)

#计算1*2*3*...*100
acc = 1
n = 1
while n <= 100:
		acc = acc*n
		n = n + 1
print(acc)
#打印 list
names = ['Micheal','Jordan','Stephen','Curry']
for name in names:
	print(name)
#打印数字 0-9
for x in range(10):
	print(x)