from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def sewing(self):
        pass


class Coat(Clothes):
    def sewing(self):
        return f'Для пошива пальто нужно: {self.param / 6.5 + 0.5 :.2f} ткани'


class Costume(Clothes):
    def sewing(self):
        return f'Для пошива костюма нужно: {2 * self.param + 0.3 :.2f} ткани'


coat = Coat(400)
costume = Costume(55)
print(coat.sewing())
print(costume.sewing())
