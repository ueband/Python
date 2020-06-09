#!/usr/bin/python
# -*- coding: UTF-8 -*-
n=1
result1 = int(input('Введите результат первого дня: '))
resultn = int(input('Введите желаемый результат: '))
print(f'Результат первого дня:  {result1}, Желаемый результат: {resultn}')
print(f'{n}-й  день:  {result1: .2f}')
print('Результат по дням:')
while result1 < resultn:
    result1 = result1*1.1
    n +=1
    print(f'{n}-й  день:  {result1: .2f}')
print(f'На {n}-й  день спортсмен достигнет результата - не менгее {resultn: .2f}')