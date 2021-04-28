#!/usr/bin/env ppython3
# -*-coding: utf-8 -*-

#input & output
print('helloworld')
print('your name?')
name = input()
print(name)

#转义符
print("hello\nnice to meet you")
print(r'hello,\n\\ nice to meet you')
print(r'''hello
nice to
meet you''')


#格式化:
# %实现格式化，%d代表整数，有几个占位符后面就对应顺序地跟几个变量
print('hi,%s,you have$%d.'%('mia',100))
#format()用传入的参数依次替换字符串内的占位符{0}、{1}
print('{0}，下降{1:.1f}%'.format('xiaoming',3.788))
#fstring
r = 2
d = 2 * r * 3.14
print(f'the surround of a circle with r={r} is{d:.2f}')
