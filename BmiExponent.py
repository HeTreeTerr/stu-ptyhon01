# -*- coding:utf-8 -*-

#输入身高
height = float(input("请输入身高(单位：米)："))
#输入体重
weight = float(input("请输入体重(单位：kg)："))
#计算 BMI 指数
bmi = weight / (height * height)

#输出 BMI 的值
print("~~~ 您的 BMI 指数为: " + str(bmi))
