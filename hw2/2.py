#!/usr/bin/python
# -*- coding: UTF-8 -*-

lst = list(input('Введите список одной строкой: '))
print(f'Вы ввели:  {lst}')
k = 0
for i in range(int(len(lst)/2)):
    lst[k], lst[k+1] = lst[k+1], lst[k]
    k += 2
print(f'Результат: {lst}')

