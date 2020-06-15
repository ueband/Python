#!/usr/bin/python
# -*- coding: UTF-8 -*-

f = open('2.txt', 'r', encoding='utf-8')
content = f.read()
print(f'Содержимое файла: \n {content} \n')
content = content.split()
print(f'Общее количество слов - {len(content)}')
f = open('2.txt', 'r')
content = f.readlines()
print(f'Количество строк в файле - {len(content)}')
f = open('2.txt', 'r')
content = f.readlines()
for i in range(len(content)):
    tmp = content[i]
    print(f'Количество слов {len(tmp.split())} \n')
print()
f.close()