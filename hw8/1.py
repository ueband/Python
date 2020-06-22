#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Data:
    def __init__(self, d_m_y):
        self.d_m_y = str(d_m_y)

    @classmethod
    def extract(cls, d_m_y):
        date = []

        for i in d_m_y.split():
            if i != '-': date.append(i)

        return int(date[0]), int(date[1]), int(date[2])

    @staticmethod
    def valid(d, m, y):

        if 1 <= d <= 31:
            if 1 <= m <= 12:
                if 9999 >= y >= 0:
                    return f'Соответствует'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Введенная дата {Data.extract(self.d_m_y)}'



print(Data('10 - 3 - 2020'))
print(Data.valid(30, 9, 2022))
print(Data.valid(1, 13, 1984))
print(Data.extract('25 - 7 - 2045'))
print(Data.extract('10 - 5 - 2020'))

