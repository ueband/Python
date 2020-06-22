#!/usr/bin/python
# -*- coding: UTF-8 -*-

from itertools import count, cycle
import rndlst

def my_count(start_n, stop_n):
    for el in count(start_n):
        if el > stop_n:
            break
        else:
            print(el)
def my_cycle(lst, iteration):
    i = 0
    iter = cycle(lst)
    while i < iteration:
        print(next(iter))
        i+=1
my_count(start_n = int(input("Введите начальное значение: ")), stop_n = int(input("Введите конечное значение: ")))
lst = rndlst.newlst(4,10)
print(lst)
my_cycle(lst, iteration = int(input("Введите число проходов: ")))
