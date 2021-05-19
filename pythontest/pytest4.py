#!/user/bin/env 
# -*-coding: utf-8 -*-ppython3

#切片练习
def trim(s):
    num1 = 0
    num2 = len(s) - 1
    if num2 == -1:
        return ''#None
    #count = 0
    while s[num1] == ' ':
        num1 = num1 + 1
        if num1 == num2:
            return ''
    #count = len(s) - 1
    while s[num2] == ' ':
        num2 = num2 - 1
    s = s[num1:num2+1]#切片，从索引num1到num2但不包含它
    return s

def trim1(s):
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s

#print(trim1('clac    '))

#迭代练习 不要被下标框住了
def findMinAndMax(L):
    if(len(L) == 0):
        return (None,None)
    min = max = L[0]
    for num in L:
        if num <= min:
            min = num
        if num >= max:
            max = num
    return(min,max)
#print(findMinAndMax([]))

#列表生成式
# l1 = [x*x for x in range(1,11)]
# L = ['HELLO','WORld',18,'aPpLe',None]
# L1 = [s.lower() for s in L if isinstance(s,str)]
# print(L1)

#生成器
#一边循环一边计算的机制,形式与列表生成式相似，但它记住的是算法
# l2 = (x*x for x in range(1,10))
# for num in l2:
#     print(num)
#Fibonacci seq of generator
def fib_gen(count):
    c,a,b = 0,0,1
    while c<count:
        #print(b)
        yield(b)#这样就定义了一个generator
        n = b
        b = a+b
        a = n
        #a, b = b, a + b同上
        c = c+1
    #print('done')
    return 'done'

#f = fib_gen(10)
#for num in f:
#    print(num)
#杨辉三角
def triangles():
    L = [1]
    n = 2
    while True:
        yield L
        TempL = []
        for c in range(0,n):#个数
            if c == 0:
                TempL.append(1)
            elif c == n-1:
                TempL.append(1)
            else:
                TempL.append(L[c-1]+L[c])
            #c = c+1 print(c)##不需要自增 for会帮你搞定
        L = TempL
        n = n+1
    
# n = 0
# results = []
# for t in triangles():
#     results.append(t)
#     n = n + 1
#     if n == 10:
#         break

# for t in results:
#     print(t)


