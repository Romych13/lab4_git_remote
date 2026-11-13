# Объявление класса
# Версия 0.0.1
class CCalculator:
    def __init__(self, x, y):
        self.x = x  # ИСПРАВЛЕНО
        self.y = y  # ИСПРАВЛЕНО

    def Sum(self):
        return self.x + self.y

    def Multiple(self):
        return self.x * self.y


# Создание объекта
Mycalc = CCalculator(3, 2)
print(Mycalc.Sum())
print(Mycalc.Multiple())