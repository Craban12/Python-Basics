class Car:
    def __init__(self, name, speed, color, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Автомобиль {self.name} поехал.'

    def stop(self):
        return f'Автомобиль {self.name} остановился.'

    def turn(self, direction):
        return f'Автомобиль {self.name} повернул {direction}.'

    def show_speed(self):
        return f'Этот супербыстрый {self.name} движется со скоростью {self.speed}.'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return 'Притормози, ты едешь очень быстро!'
        else:
            return 'Скорость в порядке.'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return 'Притормози, ты едешь очень быстро!'
        else:
            return 'Скорость в порядке.'


class PoliceCar(Car):
    pass


town = TownCar('Audi', 70, 'blue', False)
print('1:' + town.go(), town.show_speed(), town.turn('left'), town.turn('right'), town.stop())

sport = SportCar('AudiRS', 170, 'red', False)
print('2:' + sport.go(), sport.show_speed(), sport.turn('left'), sport.stop())

work = WorkCar('WAZ', 30, 'red', False)
print('3:' + work.go(), work.show_speed(), work.turn('right'), work.stop())

police = PoliceCar('Kia', 100, 'yellow', True)
print('4:' + work.go(), work.show_speed(), work.turn('right'), work.stop())
