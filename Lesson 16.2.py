class Ship:
    def __init__(self, n, p, co, m):
        self.name= n
        self.produce = p
        self.country = co
        self.model = m
    def getInfo(self):
        print(f'Корабль {self.model} пройзведен {self.produce} году')

class Frigate(Ship):
    def __init__(self, n, p, co, m, pr):
        super().__init__(n, p, co, m)
        self.price= pr
    def getInfo(self):
        super().getInfo()
        print(f'{self.name} - тип военного судного. {self.model} явяляется трехмачтовая разновидность парусного вооружения. Цена {self.price} тыс. тенге')

class Destroyer(Ship):
    def __init__(self, n, p, co, m, w ):
        super().__init__(n, p, co, m)
        self.weapon = w
    def infoPurpose(self):
        print(f'{self.name}  предназначен для борьбы с подводными лодками')
    def getInfo(self):
        super().getInfo()
        print(f'{self.name} - корабли для многоцелевых боевых быстроходных манерренных {self.model} один из первых миноносцев.')
class Cruiser(Ship):
    def __init__(self, n, p, co, m, g ):
        super().__init__(n, p, co, m)
        self.goal = g
    def infoPurpose(self):
        print(f'{self.name}  предназначен для борьбы с подводными лодками')
    def getInfo(self):
        super().getInfo()
        print(f'{self.name} - корабли для плавания по определенному маршруту {self.model} назван в честь фрегата. Историческим событием является участие в {self.goal}')


ship1 = Frigate("Фригат", 2020, "Япония", "DD-987", 12000)
ship1.getInfo()

ship2 = Destroyer("Дестрой", 1877, "Англия", "Лайтнинг" ,"миноносец")
ship2.getInfo()

ship3 = Cruiser("Крейсер", 1900, "Россия", "Аврора" , "Первой мировой войне")
ship3.getInfo()