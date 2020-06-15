#!/usr/bin/python
# -*- coding: UTF-8 -*-

total = {}
with open('6.txt', 'r', encoding='utf-8') as f:
    for i in f:   
        tmp = []        
        i = i.split()
        for k in i:            
            if k == '-': k = 0
            tmp.append(k)
            i = tmp
        subject, lecture, practice, lab = i
        total[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по предмету - \n {total}')

