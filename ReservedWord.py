# -*- coding:utf-8 -*-

"""
@Author: hss
@Date: 2026-11-21
@Description:
学习python中的保留字和标识符
"""

#导入模块
#import os
#import sys
import keyword

#获取python中的保留字
keywords = keyword.kwlist

#输出python中的保留字
print("=========保留字=========")
for keyword in keywords:
    print(keyword)