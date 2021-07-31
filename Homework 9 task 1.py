from time import sleep

class TrafficLight:
    __color = {"Красный":7, "Жёлтый":2, "Зеленый":10}
    def running(self):
        for light, time in TrafficLight.__color.items():
            print(light)
            sleep(time)

x = TrafficLight()
x.running()