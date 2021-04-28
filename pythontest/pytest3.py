#!/usr/bin/env ppython3
# -*-coding: utf-8 -*-

import math
#practice of define fun 21.04.26
def quadratic(a,b,c):
    #检测输入数据类型
    if not (isinstance(a,(int,float))&isinstance(b,(int,float))&isinstance(c,(int,float))):
        raise TypeError('bad operand type')

    if a == 0:
        return -b/c

    n = b*b - 4*a*c
    if n < 0:
        return 'no answer'
    elif n == 0:
        return -b/2/a
    else:
        x1 = (-b + math.sqrt(n))/2/a
        x2 = (-b - math.sqrt(n))/2/a
        return x1,x2

# #print(quadratic(2.0,3,1))
# #test inport --  pass
# testin = ((0,1,2),(1,0,2),(1,0,-2),(1,1,0),
# (2.0,3,1),(2,3.2,1),(2, 3, 1.5),
# (1, 3, -4),(1, -3, -4),(-1, -3, -4))
# #  ('a','b','c'),('a',1,2),(3,'a',4),(4,'a',5)

# for t in testin:
#     a = t[0]
#     b = t[1]
#     c = t[2]
#     print(quadratic(a,b,c),' ')

#参数 21.04.27
#python的参数非常灵活，有必选参数、默认参数、可变参数、关键字参数和命名关键字参数五种
#默认参数def mul(a,b=2)必须是不可变对象
#可变参数*args接收一个tuple 关键字参数**kw接收一个dict，可以直接传或者写一个tuple/dict再用*tuple/**dict告诉python
#使用命名关键字参数时如果没有可变参数需要加一个*作为分隔符
def mul(*args):
    if len(args) == 0:
        raise TypeError('null input')
    if len(args) == 1 & isinstance(args[0],(int,float)):
        return args[0]
    mul = 1
    for x in args:
        if not isinstance(x,(int,float)):
            raise TypeError('bad operand type')
        mul = mul*x
    return mul

#print(mul())

#递归 21.04.28
#汉诺塔 把n-1层移到b,最底层移到c,再把n-1层移到c
#递归尽量使用尾递归（return里不要有表达式）能够规避多层递归时栈溢出的风险
#return n * fact(n - 1) （x)    return fact_iter(num - 1, num * product) (√)
##虽然python没有针对尾递归做优化，但还是要养成好习惯
def move(n,a,b,c):
    if n == 1:
        print(a+'==>'+c)
    else:
        move(n-1,a,c,b)
        print(a+'==>'+c)
        move(n-1,b,a,c)
    return
#move(3,'A','B','C')