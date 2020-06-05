#!/usr/bin/python
# -*- coding: UTF-8 -*-

def my_f (name, surname, year, city, email, telephone):
     return ' '.join([name, surname, year, city, email, telephone])
     
if __name__ == '__main__':
    print(my_f(surname = 'Пупкин', name = 'Петя', year = '1812', city = 'Тамбов', email = 'petpup@pochta.ru', telephone = '8-800-000-00-00')) 