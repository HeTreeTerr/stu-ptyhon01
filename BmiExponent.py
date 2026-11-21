# -*- coding:utf-8 -*-

"""
@Author: hss
@Date: 2026-11-21
@Description:
BMI 指数计算器
"""

#输入身高
height = float(input("请输入身高(单位：米)："))
#输入体重
weight = float(input("请输入体重(单位：kg)："))
#计算 BMI 指数
bmi = weight / (height * height)

#输出 BMI 的值
print("~~~ 您的 BMI 指数为: " + str(bmi))

#判断身材是否合理
if bmi < 18.5:
    print("体重过轻 ~@_@~")
if bmi >= 18.5 and bmi < 24.9:
    print("体重正常 ^_^")
if bmi >= 25 and bmi < 29.9:
    print("体重过重 ~@_@~")
if bmi >= 29.9:
    print("肥胖 ~@_@~")

print("~~~"
      "感谢使用 BMI 指数计算器 ~@_@~")
