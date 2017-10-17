#!/usr/bin/env python 3
# -*- coding: utf-8 -*-
#计算a^2+b^2+c^2+...
#由于参数个数不确定，我们首先想到可以把a，b，c……作为一个list或tuple传进来
def calc(numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum
calc([1,2,3])#调用calc的时候，需要先组装出一个list或tuple
calc((1,2,3))#调用calc的时候，需要先组装出一个list或tuple
#如果利用可变参数，调用函数的方式可以简化成这样：
def calc(*numbers):#定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum
calc(1,2,3)
calc(1,3,57)
calc()
#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
#如果已经有一个list或者tuple，要调用一个可变参数，可以这样做：
nums = [1,2,3]
calc(num[0],num[1],num[2])#num[0],num[1],num[2]为List nums的下标Index。
calc(*nums)	#*nums表示把nums这个list的所有元素作为可变参数传进去。
#关键字参数
#关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
def person(name,age,**kw):	#name age为必选参数，在调用函数的时候，必须保证能接收到必选参数，**kw为关键字参数
	print('name:',name,'age:',age,'other:'kw)
person('Curry',7) #只传入必选参数
#name: Curry age: 7 other: {} 自动组装为一个dict。
person('Curry',7,city='Beijing')
person('Bob',45,gender='M',city='Chicago') #gender,city为Key,'M'和'Chicago'为Value。
#和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去：
extra = {'city': 'Mexico','addr':'China','zipcode':1234 }#dict={'Key1':Value1,'Key2':Value2,'Key3':Value3}
person('Curry',30,**extra)
#**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。

#命名关键字参数
#仍以person()函数为例，我们希望检查是否有city和job参数：
def person(name,age,**kw):
	if 'city' in kw:
		pass
	if 'job' in kw:
		pass
	print('name:',name,'age:',age,'other:',kw)
#如果要限制关键字参数的名字，就可以用命名关键字参数
def person(name,age,*,city,job):  #只接收city和job作为关键字参数,*后面的参数被视为命名关键字参数。
	print(name,age,city,job)
person('Curry',30,city='USA',job='Player')