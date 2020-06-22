#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Stationery:
    atr_title = 'Title'
    def draw(self):
        print('Запуск отрисовки.')
class Pen(Stationery):
    def draw(self):
        print('Отрисовка ручкой')
class Pencil(Stationery):
    def draw(self):
        print('Отрисовка карандашом')
class Handle(Stationery):
    def draw(self):
        print('Отрисовка маркером')

stationery = Stationery()
pen = Pen()
pencil = Pencil()
handle = Handle()
stationery.draw()
pen.draw()
pencil.draw()
handle.draw() 