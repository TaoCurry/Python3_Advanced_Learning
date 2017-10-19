#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Use EasyGUI module]
一种更简单的方法:
import easygui as g
g.XXX()
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
flavor = easygui.buttonbox('What\'s your favorite ice cream flavor?', choices= ['Vanilla', 'Chocolate', 'Strawberry'])
easygui.msgbox('You picked ' + flavor)

# model 3
import easygui
flavor = easygui.choicebox('What\'s your favorite ice cream flavor?', choices=['Vanilla', 'Chocolate', 'Strawberry'])
# easygui.choicebox()
easygui.msgbox('You picked ' + flavor)

# model 4
import easygui
flavor = easygui.enterbox('What\'s your favorite ice cream flavor?')
# 手动输入口味
easygui.msgbox('You picked ' + flavor)

# EasyGui各种功能演示

import easygui
easygui.egdemo()
# 成功调用后可以尝试拥有Easygui的各种功能，并将选择的结果打印至控制台
