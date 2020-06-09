#!/usr/bin/python
# -*- coding: UTF-8 -*-
from sys import argv

timeofwork, wages, bonus = argv
try:
    timeofwork = int(timeofwork)
    wages = int(wages)
    bonus = int(bonus)
    res = timeofwork * wages + bonus
    print(f'Заработная плата  {res}')
except ValueError:
    print('Входные данные не верны')