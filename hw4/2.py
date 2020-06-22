#!/usr/bin/python
# -*- coding: UTF-8 -*-

from random import randint
import rndlst


lst = rndlst.newlst()
print(f'Входной список: {lst}')
new = [el for el in lst if el > lst[lst.index(el)-1]]
print('Выводятся элементы исходного списка, значения которых больше предыдущего элемента.')
print(f'Выходной список: {new}')