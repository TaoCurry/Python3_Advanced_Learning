#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
PIL: Python Imaging Library,Python图像处理标准库
"""
__author__ = "Curry"

from PIL import Image
# 打开当前路径下的png图像文件
image = Image.open('D:/Python3_Advanced/ascii_dora.png')
# 获得图像的尺寸
w, h = image.size
print('Original image size: %sx%s' % (w, h))
# 缩放到50%
image.thumbnail((w//2, h//2.0))
# 把缩放后的图像用jpg格式保存
image.save('D:/Python3_Advanced/ascii_dora1.png', 'png')
