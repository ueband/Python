#!/usr/bin/python
# -*- coding: UTF-8 -*-

from itertools import count

def fibo_gen():
    old = 1
    for el in count(1):
        yield el * old
        old = el*old


j = 0
for i in fibo_gen():
    if j < 15:
        print(i)
        j += 1
    else:
        break 