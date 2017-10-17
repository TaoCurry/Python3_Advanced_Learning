#!/usr/bin/env python 3
# -*- coding:utf-8 -*-
#在函数内部，可以调用其他函数，如果一个函数在内部调用函数自身，这个函数就是递归函数。
#使用递归函数需要注意防止栈溢出。
#在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧。
#每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。
#使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。

#求n! 1*2
#1、使用迭代
def Fact(n):
	result = n
	for i in range(1,n):
		result * = i
	return result
	
def fact(n):
       result = n
       for i in range(1,n):
           result *= i
           
       return result
    
number = int(input('请输入一个正整数：'))
result = fact(number)
print('%d的阶乘是:%d'%(number,result))
#2、使用递归 
def Fact(n):
	if n == 1:
		return 1
	else:
		return n * Fact(n-1)
number = int(input('请输入一个正整数：'))
result = Fact(number)
print('%d的阶乘是:%d'%(number,result))

#3、经典的汉诺塔游戏
def Hanoi(n,x,y,z):#n表示金块的数量，x、y、z表示三个柱子。
	if n == 1:
		print('move',X,'-->' ,Z)
	else:
		Hanoi(n-1,x,z,y)	#将前n-1个金块从x移动到y上。
		Hanoi(1,x,y,z)		#将最下面的一个金块移动到z上。
		Hanoi(n-1,y,x,z)	#将y上的n-1个金块移动到z上。
	
		

