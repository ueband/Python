#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Car:
    # atributes
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        return f'{self.name} начал движение'

    def stop(self):
        return f'{self.name} остановился'

    def turn_right(self):
        return f'{self.name} повернул направо'

    def turn_left(self):
        return f'{self.name} повернул налево'

    def show_speed(self):
        return f'Скорость у {self.name} сейчас {self.speed} км/ч'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость у городского автомобиля {self.name} сейчас {self.speed} км/ч')

        if self.speed > 40:
            return f'Скорость {self.name} чем разрешенная для городского автомобиля'
        else:
            return f'Скорость {self.name} разрешенная для городского автомобиля'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость у рабочей машины {self.name} сейчас {self.speed} км/ч')

        if self.speed > 60:
            return f'Скорость {self.name} больше чем разрешенная для рабочей машины'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} это полицейская машина'
        else:
            return f'{self.name} это не полицейская машина'


subaru = SportCar(100, 'Желтая', 'Субару', False)
smart = TownCar(30, 'Белая', 'Смарт', False)
gazel = WorkCar(70, 'Зеленая', 'Газель', False)
lada = PoliceCar(110, 'Серебристая',  'Лада', True)
print(lada.turn_left())
print(f'В момент когда {gazel.turn_left()},  {lada.stop()}')
print(f'{subaru.go()} с разрешенной скоростью. {subaru.show_speed()}')
print(f'{gazel.name} {gazel.color}')
print(f'{subaru.name} полицейская машина? {subaru.is_police}')
print(f'{lada.name}  полицейская машина? {lada.is_police}')
print(subaru.show_speed())
print(lada.show_speed())
print(lada.police())
print(subaru.show_speed())
print(subaru.show_speed())