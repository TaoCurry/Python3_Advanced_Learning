#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Strings implement all of the common sequence operations, along with the additional methods described below.
Strings also support two styles of string formatting, one providing a large degree of flexibility and customization (see str.format(), Format String Syntax and Custom String Formatting) and the other based on C printf style formatting that handles a narrower range of types and is slightly harder to use correctly, but is often faster for the cases it can handle (printf-style String Formatting).
The Text Processing Services section of the standard library covers a number of other modules that provide various text related utilities (including regular expression support in the re module).
"""
__author__ = "Curry"

str.capitalize(self)       #把字符串的第一个字符大写
str.center(self, width, fillchar)       #返回一个原字符串居中,并使用空格填充至长度 width 的新字符串
str.count(sub[, start[, end]])     #返回 str 在 string 里面出现的次数,可以指定起始位置
str.encode(encoding="utf-8", errors="strict")   #以 encoding 指定的编码格式编码 string，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'
str.endswith(suffix[, start[, end]])    #检查字符串是否以suffix结尾，如果是，返回True，如果不是，返回False，可以指定起始位置
# example
>>>'Curry'.endswith('ry')
... True
>>>'Curry'.endswith('lo')
...False

str.expandtabs(tabsize=8)   #把字符串string中的tab符号转为空格，tab 符号默认的空格数是8,str也会计入tabsize中，如果str==tabsize,则会另起一个宽度为tabsize的空格
# example
>>>'01\t012\t0123\t01234'.expandtabs()
...'01      012     0123    01234'
>>>'01\t012\t0123\t01234'.expandtabs(4)
...'01  012 0123    01234'

str.find(sub[, start[, end]])   #检测sub是否包含在str中,如果存在返回最左端的索引，如果不存在返回-1
str.format(*args, **kwargs)    #格式化字符串，调用此方法的字符串必须用｛｝分隔
# example
>>>"The sum of 1 + 2 is {0}".format(1+2)
..."The sum of 1 + 2 is 3"
str.format_map(mapping)
str.index(sub[, start[, end]])  #返回子字符串sub的第一个索引，可以指定起始位置
str.isalnum()   #检查字符串是否由字母或者数字组成
str.isalpha()   #检查字符串是否由字母组成
str.isdecimal()   #检查字符串是否是十进制数组成
str.isdigit()   #检查字符串是否由数字组成
str.isidentifier()  #
str.islower()   #检查字符串
str.isnumeric() #检查字符串是否只包含数字字符
str.isprintable()   #
str.isspace()   #检查字符串是否由空格组成
str.istitle()   #检查字符串是否是标题化的
str.isupper()   #
str.join(iterable)
str.ljust(width[, fillchar] #返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串
str.lower()  #转换字符串中所有大写字符为小写.
str.lstrip([chars]) #返回一个字符串副本，其中所有的chars（默认空白字符）都被从字符串左边开始处去除。
str.partition(sep)  #
str.replace(old, new[, count])  #返回字符串副本，其中old匹配项都被替换为new,最短可以替换count个
str.rfind(sub[, start[, end]])  #检测sub是否包含在str中,如果存在返回最右端的索引，如果不存在返回-1
str.rindex(sub[, start[, end]]) #返回最右端的索引，如果不存在，抛出ValueError异常，可以定义起始位置
str.rjust(width[, fillchar])    #返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串
str.rsplit(sep=None, maxsplit=-1)   #同str.split()从右往左计数
str.rstrip([chars]) #返回一个字符串副本，其中所有的chars（默认空白字符）都被从字符串右边开始处去除。
str.split(sep=None, maxsplit=-1)    #返回字符串中所有单词的列表(list)，使用sep作为分隔符，可以使用maxsplit制定最大切分数。是join方法的逆方法.
# example
>>>'1, 2, 3'.split(',')
...['1', '2', '3']
>>>'1, 2, 3'.split()
...['1,2,3']
>>>'1+2+3+4+5'.split('+')
...['1', '2', '3', '4', '5']

str.splitlines([keepends])
str.startswith(prefix[, start[, end]])
str.strip([chars])  #返回一个字符串副本，其中所有的chars（默认空白字符）都被从字符串开始和结尾处去除,左右两侧，中间的字符串无法执行此项操作。
# example
>>>'***SPAM* for * everyone!!!'.strip('*!')
...'SPAM* for * everyone'
str.swapcase()  #返回字符串副本，其中所有的单词都交换大小写
str.title()     #返回字符串的副本，其中单次都以大写字母开头
str.translate(table)
str.upper()
str.zfill(width)    #在str的左侧以0填充width个字符

