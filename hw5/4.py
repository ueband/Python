#!/usr/bin/python
# -*- coding: UTF-8 -*-

rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_f = []
with open('4.txt', 'r', encoding='utf-8') as f:
    for i in f:
        i = i.split(' ', 1)
        new_f.append(rus[i[0]] + '  ' + i[1])
    print(new_f)

with open('4_a.txt', 'w', encoding='utf-8') as f_2:
    f_2.writelines(new_f)

    