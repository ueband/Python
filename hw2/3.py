#!/usr/bin/python
# -*- coding: UTF-8 -*-
lst = ['Зима','Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осень','Зима']
d = {12:'Зима', 1:'Зима', 2:'Зима', 3:'Весна', 4:'Весна', 5:'Весна', 6:'Лето', 7:'Лето', 8:'Лето', 9:'Осень', 10:'Осень', 11:'Осень'}
i = int(input("Введите номер месяца(от 1-12) "))
print(f'Результат из списка: {lst[i - 1]}')
print(f'Результат из словаря: {d[i]}')