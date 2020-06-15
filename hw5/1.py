#!/usr/bin/python
# -*- coding: UTF-8 -*-

tmp = []
with open('1.txt', 'w', encoding='utf-8') as f:
    l = input('Введите строку:')
    while l:
        f.writelines(l + '\n')
        l = input('Введите строку:')
    f.close()

    f = open('1.txt', 'r', encoding='utf-8')
    tmp = f.readlines()
    print(tmp)
    f.close()