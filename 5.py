#!/usr/bin/python
# -*- coding: UTF-8 -*-

revenue = int(input('Введите выручку: '))
expenses = int(input('Введите издержки: '))
print(f'Выручка:  {revenue}, Издержки{expenses}')
if revenue > expenses:
    efficiency = revenue - expenses
    print(f'Прибыль:  {efficiency}')
    rent = (efficiency/revenue)*100
    print(f'Рентабельность:  {rent}%')
    mans = int(input('Введите численность сотрудников: '))
    effofmans = efficiency/mans
    print(f'Прибыль в рассчёте на одного сотрудника:  {effofmans}')
    
elif revenue < expenses:
    print('Убыток')
else:
    print('Работаете в 0')
  