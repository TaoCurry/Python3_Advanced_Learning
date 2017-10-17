#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
def power(x):    	#计算x^2的函数
	return x * x 	#对于power(x)函数，参数x就是一个位置参数。
def power1(x,n): 	#计算x^n的函数
	s = 1			#修改后的power1(x, n)函数有两个参数：x和n，这两个参数都是位置参数。
	while n > 0:
		n = n - 1
		s = s * x
	return s	
def power2(x,n=2):	#由于我们经常计算x2，所以，完全可以把第二个参数n的默认值设定为2
	s = 1			#这样，当我们调用power(5)时，相当于调用power(5, 2)
	while n > 0:	#而对于n > 2的其他情况，就必须明确地传入n，比如power(5, 3)。
		n = n - 1
		s = s * x
	return s
#默认参数可以简化函数的调用。设置默认参数时，有几点要注意：
#一是必选参数在前，默认参数在后，否则Python的解释器会报错;
#二是如何设置默认参数。当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
#使用默认参数最大的好处是能降低调用函数的难度
def enroll(name,gender):
	print('name:',name)
	print('gender:',gender)
enroll('Curry','M')
def enroll(name,gender,age=6,city='Beijing'):
	print('name',name)
	print('gender',gender)
	print('age',age)
	print('city',city)
enroll('Curry','M')
enroll('Bob','M',7)	#除了name，gender这两个参数外，最后1个参数应用在参数age上，city参数由于没有提供，仍然使用默认值。
enroll('Sarah','F',city='Tianjin')#当不按顺序提供部分默认参数时，需要把参数名写上。意思是，city参数用传进去的值，其他默认参数继续使用默认值。						  