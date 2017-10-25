#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
    对于很多编程语言来说，程序都必须要有一个入口，比如 C，C++，以及完全面向对象的编程语言。Java，C# 等。如果你接触过这些语言，对于程序入口这个概念应该很好理解，C 和 C++ 都需要有一个 main 函数来作为程序的入口，也就是程序的运行会从 main 函数开始。同样，Java 和 C# 必须要有一个包含 Main 方法的主类来作为程序入口。
    而 Python 则有不同，它属于脚本语言，不像编译型语言那样先将程序编译成二进制再运行，而是动态的逐行解释运行。也就是从脚本第一行开始运行，没有统一的入口。
    一个 Python 源码文件除了可以被直接运行外，还可以作为模块（也就是库）被导入。不管是导入还是直接运行，最顶层的代码都会被运行（Python 用缩进来区分代码层次）。而实际上在导入的时候，有一部分代码我们是不希望被运行的。
    if __name__ == '__main__' 我们简单的理解就是： 如果模块是被直接运行的，则代码块被运行，如果模块是被导入的，则代码块不被运行。
"""
__author__ = "Curry"
# example
# 假设我们有一个 const.py 文件

PI = 3.14


def main():
    print('PI:', PI)


main()

# 直接执行该文件(python const.py),输出 PI: 3.14

# 现在，我们有一个 area.py 文件，用于计算圆的面积，该文件里边需要用到 const.py 文件中的 PI 变量，那么我们从 const.py 中把 PI 变量导入到 area.py 中

from const import PI


def calc_round_area(raduis):
    return PI * (raduis ** 2)


def main():
    print('round area:', calc_round_area(2))


main()
# 运行area.py,输出结果： PI: 3.14 round area: 12.56
# 可以看到，const 中的 main 函数也被运行了，实际上我们是不希望它被运行，提供 main 也只是为了对常量定义进行下测试.这时，if __name__ == '__main__' 就派上了用场

# fixed

PI = 3.14


def main():
    print('PI:', PI)


if __name__ == '__main__':
    main()

# 再运行 area.py, 输出如下：
# round area: 12.56
# 运行const.py  PI:3.14


# explain
# file one.py

def func():
    print('func() in one.py')


print('top-level in one.py')

if __name__ == '__main__':
    print('one.py is being run directly')
else:
    print('one.py is being imported into another module')


# file two.py
import one

print('top-level in two.py')
one.func()

if __name__ == '__main__':
    print('two.py is being run directly')
else:
    print('two.py is being imported another module')

# 执行 one.py文件
# 输出顺序
# top-level in one.py
# one.py is being run directly


# 执行 two.py文件
# 输出顺序
# top-level in one.py
# one.py is being imported into another module
# top-level in two.py
# func() in one.py
# two.py is being run directly
