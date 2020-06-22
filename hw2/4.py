#!/usr/bin/python
# -*- coding: UTF-8 -*-

lst = input("Введите строку: ").split()
print(lst)
for i in range(len(lst)):
    if len(lst[i])>10:
        print(f'{i+1}. {lst[i][:10]}')
    else:
        print(f'{i+1}. {lst[i]}')