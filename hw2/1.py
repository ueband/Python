#!/usr/bin/python
# -*- coding: UTF-8 -*-
lst = [10, 'hello', 'o', 6.0, 'T', ['Привет'], '0', True]
print(lst)
for i in range(len(lst)):
    print(f'Index {i} = {lst[i]} || type {type(lst[i])}') 