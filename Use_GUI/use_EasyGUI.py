#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Use EasyGUI module
"""
__author__ = "Curry"
# model 1
import easygui
user_response = easygui.msgbox('Hello World!')
# easygui.msgbox()创建一个消息框
print(user_response)
# OK
# model 2
import easygui
flavor = easygui.buttonbox('What\'s your favorte ice cream flavor?', choices= ['Vanilla', 'Chocolate', 'Strawberry'])
easygui.msgbox('You picked ' + flavor)