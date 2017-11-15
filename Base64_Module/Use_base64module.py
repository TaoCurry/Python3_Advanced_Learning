#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Python Base64模块介绍
Base64：用64个字符来表示任意二进制数据的方法。[其中64个字符为英文大小写(52)+数字0-9(10)+ '+' + '/']
一个Base64字符是8个 bit，但是有效部分只有右边的6个 bit。为了保证用6bit的Base64字符表示传统的8bit的字符，可以将3个传统的字节用4个base64字符表示。
如果要编码的二进制数据不是3的倍数，最后会剩下1个或2个字节，Base64用\x00字节在末尾补足后，再在编码的末尾加上1个或2个=号，表示补了多少字节，解码的时候，会自动去掉。
link：https://www.cnblogs.com/DTWolf/p/4994256.html
"""
__author__ = "Curry"

import base64

# 以"*encode"结尾的方法用于将二进制字符串转为base64编码格式的字符串，以“*decode”结尾的方法用于将base64格式的字符串重新转为二进制串。

# base64.b64encode():Encode the bytes-like object s using Base64 and return the encoded bytes.

# base64.b64decode():Decode the Base64 encoded bytes-like object or ASCII string s and return the decoded bytes.

# base64.urlsafe_b64encode():Encode bytes-like object s using the URL- and filesystem-safe alphabet, which substitutes - instead of + and _ instead of / in the standard Base64 alphabet, and return the encoded bytes. The result can still contain =. 由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数,"url safe"的base64编码，其实就是把字符+和/分别变成-和_

# base64.urlsafe_b64decode():Decode bytes-like object or ASCII string s using the URL- and filesystem-safe alphabet, which substitutes - instead of + and _ instead of / in the standard Base64 alphabet, and return the decoded bytes.


print(base64.b64encode(b'man'))    # b'bWFu'
print(base64.b64encode(b'binary\x00ssds'))   # b'YmluYXJ5AHNzZHM='
print(base64.b64encode(b'\x00'))    # b'AA==' 两个=表示补了两个字节
print(base64.b64decode(b'bWFu'))
print(base64.b64decode(b'\x00'))    # b'' b'AA==' =号在解码时自动去掉
print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))   # b'abcd++//'
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))  # b'abcd--__' 使用下划线替代/和+
