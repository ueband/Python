#!/usr/bin/python
# -*- coding: UTF-8 -*-

with open('3.txt', 'r') as f:
    tmp = []
    n_rich = []
    l = f.read().split('\n')
    for i in l:
        i = i.split()
        if int(i[1]) < 20000:
           n_rich.append(i[0])
        tmp.append(i[1])
print(f'Оклад меньше 20.000 {n_rich} \nСредний оклад {sum(map(int, tmp)) / len(l)}')
