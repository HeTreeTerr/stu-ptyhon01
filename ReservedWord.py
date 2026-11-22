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
""" print("=========保留字=========")
for keyword in keywords:
     print(keyword) """


#保留字不能作为标识符使用
#SyntaxError: invalid syntax
#else = 10

else1 = 10

"""
标识符规则
1、标识符由字母、数字、下划线组成，不能以数字开头
2、标识符不能是python中的保留字
3、标识符区分大小写
4、下划线开头的标识符有特殊含义（如单下划线表示内部使用；双下划线表示类的私有成员；以双下划线开头和结尾的标识是专有标识）
"""

print("=========标识符规则=========")
number1 = 10
Number1 = 10
NUMBER1 = 10
print(number1, Number1, NUMBER1)


#python是一种动态类型语言，变量在使用前不需要声明类型，变量的类型可以随时改变
print("=========动态类型=========")
userid = "test_0001"
print("userid:", userid, "type:", type(userid))

userid = 9527
print("userid:", userid, "type:", type(userid))

#python中，多个变量可以指向同一个值
print("=========多个变量指向同一个值=========")
a1 = a2 = a3 = 100
print("变量值：a1:", a1, "a2:", a2, "a3:", a3)
print("地址：a1:", id(a1), "a2:", id(a2), "a3:", id(a3))