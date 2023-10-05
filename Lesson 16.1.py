class Device:
    def prepered(self):
        print("Подготовить продукт")
        self.__turn_on()
        self.__grind()
        self.__switch_off()
    def __turn_on(self):
        print("Включить прибор")
    def __grind(self):
        print("Измельчить ")
    def __switch_off(self):
        print("Выключить прибор")
    def getInfo(self):
        print(f'Кухонный комбайн {self.name} {self.model}')
    def __init__(self, n, m):
        self.name = n
        self.model = m

dev = Device("Blender", "Vitek VT-8530")
dev.prepered()

class Blender(Device):
    def __init__(self, n, m, p):
        super().__init__(n, m)
        self.produce = p
    def infoPurpose(self):
       print(f'{self.name} для измельчения овщей и фруктов')

    def getInfo(self):
        super().getInfo()
        print(f'C помощью лухонного комбайна {self.name} {self.model} готовим коктейл, который произведен {self.produce} году.')

class MeatGrinder(Device):
    def __init__(self, n, m, c):
        super().__init__(n, m)
        self.cost = c
    def infoPurpose(self):
        print(f'{self.name} для измельчения мясо')
    def getInfo(self):
        super().getInfo()
        print(f'C помощью мясорубки {self.name} {self.model} готовим мясной пирог, который будет стоит {self.cost} тенге.')


d1 = Blender("Blender", "Vitek VT-8530", 2020)
d1.getInfo()


d2 = MeatGrinder("MeatGrinder", "Kitfort", 10000)
d2.getInfo()

