# -*- coding:utf-8 -*-
# @Time    : 2022/6/17 14:58
# @File    : code_practice.py
# Author: lee

"""
1.二叉树是非线性结构，栈和队列以及线性表都是线性结构，对吗？

✔
"""


"""
2.从0-99这100个数中随机取出10个，要求不能重复
"""
import random
lis = random.sample(range(100), 10)

# print(random.choice(lis))   # 序列中的一个随机数
# print(random.random())      # [0,1)之间的随机数
# print(random.randint(1, 6)) # [a, b] 之间的随机整数



"""
3.有一个列表lis=['This','is','a','Man','B','!']，
    对它进行大小写无关的排序
"""
lis1=['This','is','a','Man','B','!']
# lis1 = sorted(lis1, key=lambda x:x.lower())
lis1 = sorted(lis1, key= str.lower)
print(lis1)


"""
4.阅读以下代码，写输出结果
    lis = [2,4,5,6,7]
    for i in lis:
        if i % 2==0:
            lis.remove(i)
    print(lis)

l = [4, 5, 7]

"""


"""
5.对列表[3,1,-4,-2]按照绝对值排序
"""
l = [3,1,-4,-2]
l = sorted(l, key=lambda x:abs(x))



"""
6.现有mydict和变量onekey，
请写出从mydict中取出onekey的值的方法

a = mydict[onekey]
a = mydict.get(onekey, None)

a = mydict.setdefault(onekey, [])
这种方法：存在的话返回值，
不存在的时候创建一个值，值得内容为第二个参数+

"""


"""
7.列表中保留顺序和不保留顺序去重

"""
# 不保留顺序
lis1=[3, 1, 4, 2, 3]
# print(list(set(lis1)))

# 保留顺序
lis2=[3, 1, 4, 2, 3]
T = []
[T.append(i) for i in lis2 if i not in T]



"""
8.实现99乘法表（使用两种方法

for i in range(1,10):
    for j in range(1,i+1):
        # print('%d * %d = %d' % (i, j , i*j), end='\n')
        print('%d * %d = %d' % (j, i, i*j), end='\n')

"""


"""
9.判断dict中有没有某个key
res = False if key in dict1.keys() else True
"""


"""
10.
a = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
请问a是什么？

"""
a = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
b = list(zip(('a','b','c','d','e'),(1,2,3,4,5)))
# print(a) # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# print(b) # [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]


"""
11.将列表
alist=[{'name':'a','age':25},
{'name':'b','age':30},
{'name':'c','age':20}]，
按照age的值从大到小排列



alist = sorted(alist, key=lambda x:x['age'], reverse=True)
print(alist)
reverse = True # 降序
"""


"""
12.一个大小为100G的文件etl_log.txt，要读取文件的内容，
写出具体过程代码

with open('etl_log.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        print(line)


"""


"""
13.写代码：如何由tuple1=('a','b','c','d','e')，
和tuple2=(1,2,3,4,5)
得到res={'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

res = dict(zip(tuple1, tuple2))

"""
tuple1=('a','b','c','d','e')
tuple2=(1,2,3,4,5)
res = dict(zip(tuple1, tuple2))
# print(res)


"""
14.1<(2==2)和1<2==2的结果分别是什么？
???

"""

"""
15.如何打乱一个排好序的列表

import random
lis = [1,2,3,6,7]
random.shuffle(lis)
"""


"""
16.把a='aaabbcccdddde'这种形式的字符串，
压缩成a3b2c3d4e1这种形式。

a1 = 'aaabbcccdddde'
aa = ''
for i in sorted(set(a1)):
    aa = aa+i+str(a1.count(i))

"""


"""
17.一个数如果恰好等于它的因子之和，这个数就称为‘完数’，
比如6=1+2+3，编程找出1000以内的所有的完数

"""
def get_wanshu():
    wanshu = []

    for i in range(1, 1001): # 备选数字
        # 找因子
        s = 0
        for j in range(1, i//2+1):
            if i % j == 0:
                s += j
        else:
            if s == i:
                wanshu.append(i)
    print(wanshu)




"""
18.输入一个字符串，输出该字符串的字符的所有组合。
如输入'abc',输出a,b,c,ab,ac,bc,abc.

(不会)
"""





"""
19.给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。
给定的字符串只含有小写英文字母，并且长度不超过10000。
例如：'ababab',返回True，'ababa'，返回False

使用队列来做
"""
def _match(s):
    length = len(s)
    for i in range(1, length//2 + 1):
        if length % i == 0:
            # 可以整数，便判定是否可以组成整体
            # i 为假设的子串长度
            # s[:i] 子串
            j = 0
            print(i, j ,length)
            while s[:i] == s[j:j+i] and j + i <= length:
                j += i
            if j == length:
                return True

    return False




"""
20.使用生成器编写一个函数实现生成指定个数的斐波那契数列

不太会
"""

def fibonacci(n):

    t, a, b = 0, 0, 2

    while t < n:
        pass





"""
21.一行代码通过filter和lambda函数输出
alist=[1,22,2,33,23,32]中索引为奇数的值

"""
alist = [1,22,2,33,23,32]
alist = list(i[1] for i in ( filter(lambda x:x[0] % 2 == 1, enumerate(alist))))



"""
22.编写一个函数实现十进制转62进制，分别用0-9A-Za-z,表示62位字母

"""




"""
23.实现一个装饰器，限制该函数被调用的频率，如10秒一次


"""










"""
24.实现一个装饰器，通过一次调用，使函数重复执行5次 

"""

