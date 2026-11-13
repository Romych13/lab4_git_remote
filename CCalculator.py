# Объявление класса
class CCalculator:
    def __init__(self, x, y):
        self.x = 3  # ТУТ БАГ, который мы будем исправлять
        self.y = 2

    def Sum(self):
        return self.x + self.y

# Создание объекта
Mycalc = CCalculator(3, 2)
print(Mycalc.Sum())