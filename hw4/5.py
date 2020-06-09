#!/usr/bin/python
# -*- coding: UTF-8 -*-

from functools import reduce


def my_f(prev_el, el):
    return prev_el * el

lst = [el for el in range(100, 1001) if el % 2 == 0]
print(lst)
print(reduce(my_f, lst)) 
