#!/usr/bin/python
# -*- coding: UTF-8 -*-
import rndlst

lst = rndlst.newlst(20,40)
print(f'Входной список: {lst}')
my_lst = [el for el in lst if lst.count(el) < 2]
print(f'Выходной список: {my_lst}')