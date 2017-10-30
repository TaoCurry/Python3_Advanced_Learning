#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""

"""
__author__ = "Curry"
#
from  operator import attrgetter, itemgetter


class Student(object):
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.grade))


student_obeject = [
    Student('John', 'A', 15)
    Student('Jane', 'B', 12)
    Student('Dave', 'C', 11)
]
print(sorted(student_obeject, key=itemgetter(2)))
