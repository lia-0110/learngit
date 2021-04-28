#!/usr/bin/env ppython3
# -*-coding: utf-8 -*-

#loop pracitice in python 
# !!注意不要落下冒号!!
##ctrl+/可以注释多行

height = 1.63
weight = 55
bmi = weight/(height**2)
if bmi < 18.5:
    print('过轻')
elif bmi <= 25:
        print("正常")
elif bmi <= 28:
    print("过重")
elif bmi <= 32:
          print("肥胖")
else:
     print("严重肥胖")

sum = 0
for x in range(101):
    sum = sum + x
print(sum)
print(x)
while sum > 5000:
    x = x + sum -5000
    sum = sum - 1
print(x)

for x in range(10):
    if x % 2 == 0:
        continue
    print(x)

num = 0
while num < 20:
    num = num + 1
    print(num)
    if num >= 10:
        print('END')
        break
    
#while num == 10:
#    print('这是一个死循环，CTRL+C结束它')