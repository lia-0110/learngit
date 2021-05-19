#!/user/bin/env
# -*-coding: utf-8 -*-ppython3
 
#高阶函数（将函数作为参数传入的一种函数
#函数式编程就是指这种高度抽象的编程范式

#map()练习
#map(func,iterable),对后者执行前者
#它返回iterator，是惰性的，需要结果时要用list()获得
##利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
def normalize(name):
    #return name.capitalize()
    return name.title()#首字母大写其余小写
    #return(name[0].upper() + name[1:].lower())#upper大写 lower小写

#L1 = ['adam', 'LISA', 'barT']
#L2 = list(map(normalize, L1))
#print(L2)

#reduce()练习
#reduce(func,iterable),对后者叠加地执行前者
##请编写一个prod()函数，可以接受一个list并利用reduce()求积
from functools import reduce
def prid(L):
    def f(x,y):
        return x*y
    return reduce(f,L)
#print(prid([1,3,5]))

#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
def str2float(str):
    dic = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    #DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    def str2num(s):
        return dic[s]
    def num2float(x,y):
        return x*10.000+y
    str = str.replace('.','')#先换后除，有位数上的局限性
    num = reduce(num2float,map(str2num,str))/1000.000
    return num
#print(str2float('123.456'))

def str2float2(str):
    dic = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    def str2num(s):
        return dic[s]
    def num2floatleft(x,y):
        return x*10.000+y
    def num2floatright(x,y):
        return x/10.000+y
        #return x+y/10这里正向的x+y/10不能实现期望的功能，
        #问题在于y/10只有一次，即新的后一位总是一位小数，
        #即得到的是4+0.5+0.6+0.7……
    s = str.split('.')#以小数点为界切成两片
    #s[1][::-1] s[1]的倒置
    num = reduce(num2floatleft,map(str2num,s[0])) + (reduce(num2floatright,map(str2num,s[1][::-1])))/10
    return num
#print(str2float2('123.45678'))

#filter()
#filter(func,iterable)传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
#它返回iterator，是惰性的，需要结果时要用list()获得
##请利用filter()筛选出回文数
def is_palindrome(n):
    #转换成str判断
    s = str(n)
    x = s[::-1]
    #filter()
    return s == x
#print(list(filter(is_palindrome,range(1,1000))))

#sort()
#sort()可以接受一个key函数来实现自定义排序，对L中的每一个对象逐一执行key函数的操作
#这里注意key函数不是对整个L操作
L = [('Bob',75),('adam',60),('Lisa',90),('tia',89)]
def by_name(t):
    return t[0].title()#对L中的每一个t取t[0]
def by_score(t):
    return t[1]
#print(sorted(L,key=by_name))#从高到低
#print(sorted(L,key=by_score,reverse=True))
