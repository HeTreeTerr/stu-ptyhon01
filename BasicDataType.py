# -*- coding:utf-8 -*-

"""
@Author: hss
@Date: 2026-11-24
@Description:
基础数据类型
"""

#数字类型
print("=========数字类型========")

#整数
a1 = -2017
a2 = 0
a3 = 5
print("a1:", a1, "type:", type(a1))
print("a2:", a2, "type:", type(a2))
print("a3:", a3, "type:", type(a3))

#进制转换
print("=========进制转换========")
#二进制 以0b/0B开头
b1 = 0B1101
#八进制 以0o/0O开头
b2 = 0o17
#十进制 以非0开头
b3 = 123
#十六进制 以0x/0X开头
b4 = 0x1A
print("b1:", b1, "type:", type(b1))
print("b2:", b2, "type:", type(b2))
print("b3:", b3, "type:", type(b3))
print("b4:", b4, "type:", type(b4))


#浮点数
print("=========浮点数========")
c1 = 3.14
c2 = -2.5
c3 = 0.0
print("c1:", c1, "type:", type(c1))
print("c2:", c2, "type:", type(c2))
print("c3:", c3, "type:", type(c3))

#科学技术法
c4 = 2.7e2
c5 = -3.14e5
c6 = 6.16e-2
print("c4:", c4, "type:", type(c4))
print("c5:", c5, "type:", type(c5))
print("c6:", c6, "type:", type(c6))

#复数
d1 = 3 + 4j
d2 = 5 - 2j
print("d1:", d1, "type:", type(d1))
print("d2:", d2, "type:", type(d2))
print(d1 + d2)

#字符串
print("=========字符串========")
e1 = "Hello, World!"
e2 = 'Python'
e3 = """This is a multi-line string.
It can span multiple lines."""
e4 = '''This is another multi-line string.
It can also span multiple lines.'''

print("e1:", e1)
print("e2:", e2)
print("e3:", e3)
print("e4:", e4)

#转义符
f1 = "Hello, \"Python\"!"
f2 = r"Hello, \"Python\"!"
f3 = R"Hello, \"Python\"!"
print("f1:", f1)
print("f2:", f2)
print("f3:", f3)

#布尔类型
print("=========布尔类型========")
g1 = True
g2 = False
print("g1:", g1, "type:", type(g1))
print("g2:", g2, "type:", type(g2))