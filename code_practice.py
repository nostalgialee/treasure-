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
# lis1=[3, 1, 4, 2, 3]
# print(list(set(lis1)))

# 保留顺序
lis2=[3, 1, 4, 2, 3]
T = []
[T.append(i) for i in lis2 if i not in T]






"""
8.实现99乘法表（使用两种方法）

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
"""

def fibonacci(n):
    t, a, b = 0, 0, 1
    # 使用生成器节约空间
    while t < n:
        yield b
        a, b = b, a + b
        t += 1

# for i in fibonacci(23):
#     print(i)


"""
21.一行代码通过filter和lambda函数输出
alist=[1,22,2,33,23,32]中索引为奇数的值


alist = [1,22,2,33,23,32]
alist = list(i[1] for i in ( filter(lambda x:x[0] % 2 == 1, enumerate(alist))))

"""





"""
22.编写一个函数实现十进制转62进制，分别用0-9A-Za-z,表示62位字母


import string
print(string.ascii_lowercase) # 小写字母
print(string.ascii_uppercase) # 大写字母
print(string.digits) # 0-9

s=string.digits+string.ascii_uppercase+string.ascii_lowercase
print(s)
#


def _10to62(num):
    ss = ''
    while True:
        # 每一位的数字转化
        ss = s[num%62] + ss
        print("s[num%62]", s[num%62])
        if num // 62 == 0:
            # break
            return ss
        num = num // 62 # 得到几个轮回
        # 假如 整除结果小于62, 循环终止
        # 假如 整除结果大于62，需要继续整除 62,得到有几轮，
        # 但是轮回也需要用62进制表示，直至 整除至 num == 0

print(_10to62(666))


"""







"""
23.实现一个装饰器，限制该函数被调用的频率，如10秒一次

import time
from functools import wraps

def dec(func):

    func_name = func.__name__
    cache = {func_name: None}

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = None
        if cache.get(func_name) is None:
            # 未被执行过
            cache[func_name] = time.time()
            result = func(*args, **kwargs)
            print('function is running')

        else:
            start_time = cache.get(func_name)
            now_time = time.time()
            time_interval = now_time - start_time
            if time_interval >= 10:
                cache[func_name] = now_time
                result = func(*args, **kwargs)

            else:
                print('function cant run for a while')
        return result

    return wrapper


@dec
def add(x, y):
    print(x + y)


add(1, 2)
add(1, 3)
time.sleep(10)
add(3, 4)


"""






"""
24.实现一个装饰器，通过一次调用，使函数重复执行5次

from functools import wraps

def dec(func):
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = [func(*args, **kwargs) for i in range(5)]
        return result
    return wrapper

@dec
def add(x, y):
    print(x + y)

add(1, 2)

"""




"""
25.请编写一个函数将ip地址转换成一个整数。
如10.3.9.12转换成00001010 00000011 00001001 00001100，然后转换成整数


def _ip2int(ip):
    lst = ip.split('.')
    print(lst)
    to_bin = []
    for i in lst:
        # Python zfill() 方法返回指定长度的字符串，原字符串右对齐，前面填充0。
        to_bin.append(bin(int(i))[2:].zfill(8))


        print(to_bin)
        print(int(''.join(to_bin), 2))

    return int(''.join(to_bin), 2) # 

# class int(x, base=10)
    # 参数
    # x -- 字符串或数字。
    # base -- 进制数，默认十进制。
    # base 是 前面 x 的进制


print(_ip2int("10.3.9.12"))


"""







"""
26.求以下代码结果
def num():
    return [lambda x:i*x for i in range(4)]
    
    [0*x, 1*x, 2*x, 3*x]
    
print([m(2) for m in num()])

[0, 2, 4, 6]




其实相当于如下的代码
def num():
    sub = []
    for i in range(4):
        def num2(x):
            return x * i
        sub.append(num2)
    return sub

print([m(2) for m in num()])  


[6, 6, 6, 6]

"""






"""
27.求以下代码的输出结果
collapse=True
processFunc=collapse and (lambda s:' '.join(s.split())) or (lambda s:s)
print(processFunc('i\tam\ntest\tproject!'))


# True and 'i am test project!' or 'i   am  test    project!'
先看 or 两边, ===> 'i am test project!' or 'i   am  test    project!'
得到：
'i am test project!' 




collapse=False
processFunc=collapse and (lambda s:' '.join(s.split())) or (lambda s:s)
print(processFunc('i\tam\ntest\tproject!'))

# False and 'i am test project!' or 'i   am  test    project!'

先看 or 两边，
False or 'i   am  test    project!'
得到：
'i   am  test    project!'

"""






"""
28.
编写一个函数，找出数组中没有重复的值的和

def func2(lis):
    return sum([i for i in set(lis) if lis.count(i) == 1])

print(111, func2([3, 4, 1, 2, 5, 6, 6, 5, 4, 3, 3]))

"""








"""
29.下面代码的执行结果是

a=1
def bar():
    # a+=3
    
bar()
print(a)

报错

"""






"""
30.写一个函数，计算出以下字母所代表的数字，每个字母值不一样
题没看明白

"""







"""
31.写出如下代码的输出结果
def decorator_a(func):
    print('Get in decorator_a')
    def inner_a(*args, **kwargs):
        print('Get in inner_a')
        return func(*args, **kwargs)
    return inner_a
    
def decorator_b(func):
    print('Get in decorator_b')
    def inner_b(*args, **kwargs):
        print('Get in inner_b')
        return func(*args, **kwargs)
    return inner_b
    

@decorator_b #f=decorator_b(f)
@decorator_a #f=decorator_a(f)
def f(x):
    print('Get in f')
    return x * 2


被装饰函数定义阶段：
    例子中：
    先走 a 
    后走 b
decorator_b(decorator_a(f))

decorator_a(f) 作为被装饰函数 放入 decorator_b 中
内部 inner 中的伪代码
    def inner_b(*args, **kwargs):
        print('Get in inner_b')
        return decorator_a(f)

被装饰函数执行阶段：
    例子中 
    先走 b
    后走 a

打印结果：

'Get in decorator_a'
'Get in decorator_b'
'Get in inner_b'
'Get in inner_a'
'Get in f'


"""








"""
32.写出以下代码的输出结果：

def test():
    try:
        raise ValueError('something wrong')
        # 抛出异常直接到下面异步
    except ValueError as e:
        print('error occured')
        return
    finally:
        print('ok')
test()

结果：

error occured
ok


"""






"""
33.求出以下代码的输出结果
mydict={'a':1,'b':2}
def func(d):
    d['a']=0
    return d
    
func(mydict)
mydict['c']=2
print(mydict)


>>> {'a':0,'b':2, 'c':2}


"""






"""
34.写个函数接收一个文件夹名称作为参数，
显示文件夹中文件的路径，以及其中包含的文件夹中文件的路径

import os

def _path(dirname):
    lis_dir = os.walk(dirname)

    for root, dirs, files in lis_dir:
    
        for d in dirs:
            print(os.path.join(root, d))
        for f in files:
            print(os.path.join(root, f))
            
            
"""






"""
35.输入某年某月某日，判断这是这一年的第几天

先不做了
"""



"""
36.写一个的支持with语句的类

类中必须实现 __enter__ / __exit__ 方法，才能支持
with语句

class Wclass:
    
    def __enter__(self):
        pass
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        # 发生错误也要进行的操作
        pass
"""





"""
37.实现一个单例模式。(尽可能多的方法)
class MetaClass(type):

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls, *args, **kwargs)
        return obj

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._instance = None

    def __call__(self, *args, **kwargs):
        if  self._instance:
            return self._instance
        self._instance = self.__new__(self)
        self.__init__(self._instance,  *args, **kwargs)
        return self._instance


import threading

class SingletonType(type):
    _instance_lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with SingletonType._instance_lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super().__call__(*args, **kwargs)
        return cls._instance



class Singleton(metaclass=MetaClass):

    def __init__(self):
        pass


s1 = Singleton()
s2 = Singleton()
print(s1)
print(s2)

"""

class SingleObjectType(type):

    def __new__(cls, *args, **kwargs):
        cls_obj = super().__new__(cls, *args, **kwargs)
        return cls_obj

    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance:
            return self.__instance
        self.__instance = self.__new__(self)
        self.__instance.__init__(*args, **kwargs)
        return self.__instance


class A(metaclass=SingleObjectType):

    a = 1

    def __init__(self):
        pass

# a1 = A()















"""
38.手写一个栈
#给一个点，我们能够根据这个点知道一些内容

"""
class Node:

    def __init__(self,val): #定位的点的值和一个指向
        self.val=val #指向元素的值,原队列第二元素
        self.next=None #指向的指针


class Stack:

    def __init__(self):
        self.top = None

    def push(self, item):
        node = Node(item)
        if not self.top:
            self.top = node
        else:
            node.next = self.top
            self.top = node

    def pop(self):
        if not self.top:
            return None
        pop_item = self.top
        self.top = self.top.next
        return pop_item.val




"""
39.使用两个队列实现一个栈
class Stack:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, node):
        self.q1.append(node)

    def pop(self):
        if not self.q1:
            # 删完了
            return None
        while len(self.q1) > 1:
            node = self.q1.pop(0)
            self.q2.append(node)
        pop_node = self.q1.pop(0)
        self.q1, self.q2 = self.q2, self.q1
        return pop_node


st=Stack()
print(st.pop())
st.push(1)
print(st.pop())
st.push(1)
st.push(1)
st.push(1)
print(st.pop())
print(st.pop())
print(st.pop())

"""

class Stack1:
    # 先进后出
    def __init__(self):
        self.queueA = [] # 队列
        self.queueB = []

    def push(self, item):
        self.queueA.append(item)

    def pop(self):
        if not self.queueA:
            return None
        while len(self.queueA) != 1:
            item = self.queueA.pop(0)
            self.queueB.append(item)
        pop_item = self.queueA.pop(0)

        while self.queueB:
            item = self.queueB.pop(0)
            self.queueA.append(item)
        return pop_item



# st=Stack()
# print(st.pop())
# st.push(1)
# print(st.pop())
# st.push(1)
# st.push(2)
# st.push(3)
# print(st.pop())
# print(st.pop())
# print(st.pop())






























"""
*****************************************************
40.有如下链表类，请实现单链表逆置。
*****************************************************
"""
class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None

class Solution:

    # pHead ---> p1 ---> p2 ---> p3 ---> p4
    #            tmp
    def reverseList(self, pHead):
        if not pHead or pHead.next:
            return pHead
        last = None
        while pHead:
            # TODO: 这个不太熟练
            pass
            tmp = pHead.next
            pHead.next = last
            last = pHead
            pHead = tmp
        return last



"""
41.手写一个队列
环形队列

"""
class Queue:

    def __init__(self, size):
        self.q = [0 for i in range(size)]
        self.size = size
        self.front = 0
        self.near = 0

    def push(self, item):
        if self.is_full():
            raise IndexError('queue is full')
        self.near = (self.near + 1) % self.size
        self.q[self.near] = item

    def pop(self):
        if self.is_empty():
            raise IndexError('queue is empty')
        item = self.queue[self.front]
        self.front = (self.front + 1) % self.size
        return item


    def is_full(self):
        return (self.near + 1) % self.size == self.front

    def is_empty(self):
        return self.front == self.near













#ps: 不会的东西总结：
    # 迭代器生成器 (✔)

    # 装饰器 (✔)

    # 元类（知识点）(对)
    # meta

    # 并发编程相关 (基本✔)


    # 网络编程

    # 数据库
        # 主要是 索引相关

