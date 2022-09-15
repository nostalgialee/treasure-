# -*- coding:utf-8 -*-
# @Time    : 2022/6/21 21:37
# @File    : practice.py
# Author: lee


# 循环一个列表

li = [1,2,3,43,]

def generation(li):
    yield from li
#
# for i in generation(li):
#     print(i)





# 编写一个生成器，
# 将一个二维的列表转化为一维的列表。


li2 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

def generation2(li2):
    for i in li2:
        for j in i:
            yield j


# for i in generation2(li2):
#     print(i)

# 处理成列表

l = list(generation2(li2))
print(l)
