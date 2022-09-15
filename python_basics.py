# -*- coding:utf-8 -*-
# @Time    : 2022/6/17 14:59
# @File    : python_basics.py
# Author: lee


"""
1.描述以下字典的items()方法和iteritems()方法有啥不同？
items() 将键值对以[key, value]返回，字典无序，所以返回的字典的所有项目也没有顺序
iteritems() 返回的是迭代器

"""


"""
2.请列举你所知道的python代码检测工具以及他们之间的区别

pylint --- 源代码分析器，可以分析python代码中的错误 (这个用过)
pyflakes --- 检查源文件错误的简单程序，不会检查代码风格。
pep8 --- 检查代码规范的工具

"""



"""
3.介绍一下try except的用法和作用
异常处理异常捕获

    try:
        Normal execution block
        
    except A:
        Exception A handle
        
    except b:
        Exception A handle
        
    except:
        Other exception handle
    
    else:
        if no exception,get here
        # 没有错误
    finally:
        print("finally")
                
"""


"""
4.获取python解释器版本的方法
python -V
"""



"""
5.在python中如何拷贝一个对象，并说明他们之间的区别
赋值：创建了对象的一个新的引用
修改其中任意一个变量都会影响到另一个

浅拷贝：
import copy
copy.copy()
创建一个新对象（拷贝），但是对象内部依旧沿用原来的引用
更改新对象内部对象，
    原对象内部（可变数据类型）对象也会改变
    原对象内部（不可变数据类型）对象不会改变


深拷贝：
import copy
copy.deepcopy()
创建一个新的对象（拷贝），并且递归复制其内部所包含的对象
更改新对象内部对象，
    原对象内部（可变数据类型）对象不会改变
    原对象内部（不可变数据类型）对象不会发生改变

"""







"""
6.python中进制转换:

进制转换以十进制为媒介 
十六进制前面加上0x，八进制加上0o，二进制前面加上0b

type(x) == int
    不能有 base 参数，否则报错
type(x) == str
    base 可有可无，
    存在的时候，x 是为 base 进制的数字，将其转化为 十进制



        二进制             八进制             十进制             十六进制
    
二进制                  bin(int(x,8))     bin(int(x, 10))      bin(int(x, 16))

八进制   oct(int(x,2))                    oct(int(x,10))       oct(int(x,16))

十进制   int(x, 2)      int(x,8))                              int(x, 16)

十六进制  hex(int(x,2))  hex(int(x,8))    oct(int(x,10))

下表中， x是 str 类型

"""







"""
7.关于Python程序的运行方面，有什么手段能提升性能？

    1.使用多进程，充分利用机器的多核性能
    2.对于性能影响较大的代码，使用 c/c++ 编写
    3.对于 IO 阻塞造成的性能影响，可以使用 IO 多路复用解决
    
    4.尽量使用python的内置函数，使用局部变量 （**********）


"""





"""
8.python是如何进行内存管理的？python的程序会内存泄漏吗？
说说有没有什么方面阻止或者检测内存泄漏？






"""


"""
9.python代码如何获取命令行参数
sys.argv
getopt模块

"""




"""
10.如何查找一个字符串中特定的字符？find和index的差异？

find() 查找子字符串，找到返回元素索引，找不到返回 -1
index() 在字符串中查找子串第一次出现的位置，找不到子串，抛异常

"""




"""
11.python递归的最大层数？
1000、999、998、997

"""





"""
12.filter、map、reduce的作用？
    
    # 排序函数
    sorted(iterable, key=function, reverse=False)

    filter 过滤函数
    filter(function, iterable)
        
    map    映射函数
    map(function, iterable)
        s=map(lambda x,y:x+y,range(10),range(10))
        ss=map(lambda x:x*x,range(10))
        
    reduce 
    reduce(function, iterable)
    
    1.可迭代对象的第一个数和第二个数当成x和y
    2.将第一次函数的执行结果当成x，然后再传入一个数当成y
    3.再执行函数

"""





"""
13.什么是闭包
    1.嵌套函数
    2.内部函数引用外部的非全局变量

def func():
    a = 1
    def inner():
        return a
    return inner


"""






"""
14.简述生成器，迭代器，装饰器以及应用场景
    
    迭代器
        拥有 __iter__() 与 __next__()方法
        从容器的第一个元素开始访问，直至所有元素被完全访问    
    生成器
        本质是迭代器，一个函数调用时返回一个迭代器，
        这个函数就叫生成器。通常带有yield
    装饰器
        闭包，开放封闭原理

"""




"""
15.生成器与函数的区别？
    1. 函数：return 
    2.yield value 同时标记或记忆 point of the yield
    以便于在下次调用时从标记点恢复执行，yield 使函数转换成
    生成器，

"""




"""
16.列表推导式[i for i in range(10)]和
生成式表达式(i for i in range(10))的区别

[i for i in range(10)] 列表
(i for i in range(10)) 迭代器
它一次处理一个对象，而不是一口气处理和构造整个数据结构，
可以节约内存。

"""




"""
17.python如何定义函数时如何书写可变参数和关键字参数？

def func(a, *args, b=None, **kwargs):
    pass

"""




"""
18.python中enumerate的意思是什么？
枚举
"""




"""
19.描述以下dict的items和iteritems的区别
items() 返回 列表
iteritems() 返回迭代器 python 中没有 iteritems()
"""





"""
20.是否使用过functools中的函数？他的作用是什么？
from functools import wraps
    在装饰器中用过，如果不使用wraps，
    则原始函数的__name__和__doc__的值就会丢失
    
from functools import reduce
    第一个参数是一个函数，
    第二个参数是一个可迭代对象，代码如下：
    
from functools import reduce
a=reduce(lambda x,y:x+y,range(10))
print(a) 
"""





"""
21.如何判断一个值是方法还是函数
    1.type() 进行判断
    2.与类和实例无绑定关系的function都属于函数（function）
    3.与类和实例有绑定关系的function都属于方法（method）

"""




"""
22.lambda表达式格式以及应用场景？
    lambda 参数：返回表达式

    应用场景：常见的在filter，reduce以及map中使用

"""





"""
23.pass的使用
占位语句，无实际意义
"""




"""
24.*arg和**kwargs的作用
    用来接收不确定个数的参数
    位置参数与关键字参数

"""





"""
25.如何在函数中设置一个全局变量？
a = 1
def func():
    global a
    a += 1
    return a
    
print(a)
"""




"""
26.yield from 和 yield 的区别
def a():
    for i in [1,2,3,4]:
        yield i
等价于
def b():
    yield from [1,2,3,4]

for i in a():
    print(i)
    
for i in b():
    print(i)

"""


"""
****************************
27.re的match和search的区别
    match() 
        函数是在string的开始位置匹配，
        如果不匹配，则返回None        
        match()只有在0位置匹配成功的话才有返回，

    search()
        会扫描整个string查找匹配；

方便记忆，match 匹配，从0为值开始匹配，0位置匹配成功才成功
        search 搜索，范围大，所以需要整个string范围内查找
"""




"""
28.什么是正则的贪婪匹配？贪婪模式和非贪婪模式的区别
贪婪匹配
    正则表达式中，尽可能匹配更多的字符
非贪婪匹配
    匹配到结果即可

"""





"""
*************************************

29.如何使用python删除一个文件或者文件夹？
os.remove() # 删除文件
os.removedirs() # 删除空文件夹

import shutil
shutil.rmtree() # 删除文件夹

*************************************
"""






"""
************************************* 需要后续好好了解总结
30.logging模块的作用以及应用场景

logging模块定义的函数和类为应用程序和库的开发实现了
一个灵活的事件日志系统。记录日志

*************************************
"""





"""
31.json序列化时可以处理的数据类型有哪些？

string、int、list、tuple、dict、bool、null

如何定制支持datetime类型？序列化时，
遇到中文转成unicode，如何保持中文形式？
"""





"""
32.写出邮箱的正则表达式

r‘^.+@.+\.com$’ 这个不对。 . 表示所有字符，不符合题义

p = r'^[0-9a-zA-Z]+@[0-9a-zA-Z]+\.com$'
import re
print(re.match(p, "842109551@qq.com"))
print(re.match(p, "lhow5377@gmail.com"))


"""






"""
33.写python爬虫分别用到了哪些模块？分别有什么用？
"""






"""
*********************************************
34.sys.path.append('xxx')的作用

    添加搜索路径
    对于模块和自己写的脚本不在同一个目录下，
    在脚本开头加sys.path.append('xxx')：
    import sys
    sys.path.append(’引用模块的地址')
    
    这种方法是运行时修改，脚本运行后就会失效的。
********************************************* 不会的

"""







"""
35.简述面向对象的三大特性？

    继承:
        1.继承的类直接拥有被继承的类的属性与方法而不需要重写
        被继承的类：父类，基类
        继承的类：子类，派生类
        单继承、多继承（python中独有的继承方式）
        
        多继承：
            py2
                不自动继承 object, 默认为经典类
                显式继承 object 为新式类
                类之间的寻找方法遵循深度优先
                没有 super() 与 mro()

            py3
                自动继承object --- 默认新式类
                类之间的寻找方法遵循广度优先
                c3算法有
                有 super() 与 mro()
                
    
    
    封装: --- 
        狭义上：--- 将类中的属性与方法定义为私有
        封装就是把 属性 与 方法 私有化
        父类私有化的属性与方法，子类无法修改
        
    
    
    
    多态：一个类能出现多种形态
        
        多态就是 不同的对象，可以调用相同的方法，得到不同的结果
    
    
        多态就是不同的对象可以调用相同的方法然后得到不同的结果，在python中
        处处都是多态，ex: 列表与string都可以使用 + 和 *
        python 中传递对象类型的时候不需要明确定义，数据类型不需要继承来维护统一

"""











"""
36.什么是鸭子模型？

    ***对象之间的关系不需要继承来维护，而是通过约定俗成的规定***

    当我们传递对象作为参数的时候，可能有多个类型的对象作为参数被传递，
    我们在语言中需要描述清楚对象是属于那个类的对象
    可以通过继承的方式，约定一个父类，作为这些被继承的对象的父类
    但是 python 中，在定义对象的时候不需要明确定义，所以python中处处是多态
    对象的类型不需要继承来维护
    

    动态类型风格
    一个对象的定义：
        1.不是有继承自特定的类或者实现特定的接口，
        2.而是有其属性与方法的集合决定
    ex: 迭代器的定义：
        拥有 __iter__ 与 __next__ 方法
        
"""






"""
37.super的作用
    当子类中的方法与父类中的方法重名时，子类会覆盖父类的方法
    使用情景：
        同时想调用父类方法与子类的方法的时候
        
    当子类的方法与父类重名的时候，子类会覆盖弗雷德方法，
    当我们想要在子类中调用父类的方法的时候，就用 super().func()

"""





"""
38.mro是什么？ --- Method Resolution Order，或MRO

    当编程语言支持继承的时候，其方法可以定义在当前类，也可以定义在父类。
    所以在方法调用的时候 ***需要对当前类和基类进行搜索来确定方法坐在的位置**
    mro --- 方法解析顺序

"""





"""
39.什么是c3算法？

    c3算法是python ---新式类中--- 用来产生mro顺序的一套算法。
    即多继承的查找规则
    在 新式类中，产生 mro 顺序的一套算法，即多继承的搜索规则
    
"""




"""
40.列举面向对象中带双下划线的特殊方法

    ********************************************************    
    __new__()
         可以调用其它类的构造方法或者
         直接返回别的对象来作为本类的实例
    
    __init__()
        类的实例化
    
    __delete__()
        采用del删除属性时，触发
    
    __call__()
        对象后边加括号，触发执行 
    
    __str__()
        print打印一个对象时
    
    __repr__
        print打印一个对象时, 'str'
    
    __doc__：
        类的注释，该属性是无法继承的。

    __setattr__()
    __getattr__()
    __delattr__()
    

"""




"""
41.双下划线和单下划线的区别

双下划线
    私有变量或方法 --- 只有类内部可以被调用

单下划线
    保护成员 --- 只有类对象和子类对象可以访问
"""




"""
42.实例变量和类变量的区别

    实例变量:
        每个实例独有的数据
    
    类变量:
        是该类所有的实例共享的数据（属性和方法）
        
"""






"""
43.实例方法、静态方法和类方法的区别


    实例方法：
        def func(self, *args, **kwargs):
            pass
        只有实例可以调用
    
    静态方法
        @staticmethod
        def func():
            # 没有参数
            # 实例与类都可以调用
            return
        
    类方法：
        @classmethod
        def func(cls, *args, **kwargs):
            # cls 指向类
            # 实例与类都可以调用
            return
        
    
"""




"""

44.isinstance和type的作用
    
    1.判断对象的类型
    2.isinstance 可以判断继承关系，type 不可以
    
    
"""






"""
45.使用with语句的好处是什么

    使用 with 语句之后，结构体内的代码出现错误的时候，都会对当前对象进行清理工作
    
    使用 with 语句的前提是 --只有支持上下文管理器的对象才能使用with--，
        即对象内部实现了
        __enter__
        __exit__ 方法
    
    
    class A:
    
        def __enter__(self):
            print('进入with语句')
            return self # 返回self就是把这个对象赋值给as后面的变量
                 
        def __exit__(self):
            # 进行对象的处理工作
            
            pass
    
    
    举例子：
    
        with open('a.txt', 'r') as f:
            f.read()
        # with中出现任何错误，都会执行file.close（）方法
    
        class F:
            
            def __exit__():
                self.close() # 文件的关闭在 __exit__中执行，所以 with 语句可以不执行f.close()
        
        
"""

# 写一个的支持with语句的类

class WithObject:

    def __enter__(self):

        return self # 返回self就是把这个对象赋值给as后面的变量

    def __exit__(self, exc_type, exc_val, exc_tb):
        # TODO:
        pass






"""
46.如何判断一个对象是否可调用？
    哪些对象是可调用对象？如何定义一个类，使其对象本身就是可调用对象？
    
    callable(obj) 
    
    对象所属类中定义了 __call__ 方法的，其本身就是可调用对象
    
   哪些对象是可调用对象？
   类中含有 __call__ 方法
   

   如何定义一个类，使其对象本身就是可调用对象？
    class A:
        
        def __call__():
            pass

"""








"""
47.类的加载和实例化过程


类:命名空间
        -------
       |       |
       |       |
       |       |
       |_______|

对象：命名空间
对象自己的命名空间没有的属性，要向类命名空间中找
对象自己的命名空间有的属性，要向自己的命名空间中找
        -------
       |       |
       |       |
       |       |
       |_______|


    类与对象存储两块内存空间之中
    类的加载：由上而下依次加载
    实例化的过程：
        1.创造一块空间 __new__
        2.执行__init__
        3.类名指向这块空间
        
        
    ***********************************    
    1.在堆内存中生成 class 对象，把静态变量和静态方法加载到方法区，
        这个堆内存中的class对象是方法区数据的入口
        
    2.静态变量默认初始化
    3.静态变量显式初始化
    4.执行静态变量代码
    5.成员变量默认初始化，显式初始化
    
    
    
    6.执行构造函数
    



    
    ***********************************    

"""






"""

# 这个不会的
13.IO多路复用的作用？

select、poll、epoll模型的区别

"""

