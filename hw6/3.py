#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Worker:
    name = None
    surname = None
    position = None
    profit = None
    bonus = None

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
    def get_name(self):
        return self.name + ' ' + self.surname
    def get_full_wage(self):
        self.__income = {'wage': self.wage, 'bonus': self.bonus}
        return self.__income

manager = Position('Ирина', 'Иванова', 'Инженер', 25000, 10000)
print(manager.get_name(), manager.get_full_wage()) 