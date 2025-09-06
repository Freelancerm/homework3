import math


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        """ Додавання двох векторів """
        if not isinstance(other, Vector):
            raise TypeError("Додавання можливе лише з іншим об'єктом Vector")
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        """ Віднімання двох векторів"""
        if not isinstance(other, Vector):
            raise TypeError("Віднімання можливе лише з іншим об'єктом Vector")
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        """ Множення вектора на число """
        if not isinstance(scalar, (int, float)):
            raise TypeError("Множення можливе лише на число")
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    def length(self):
        """ Обчислює та повертає довжину вектора """
        return round(math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2), 2)

    def __lt__(self, other):
        """" Порівнює вектори за довжиною (менше) """
        if not isinstance(other, Vector):
            raise TypeError("Порівняння можливе лише з іншим об'єктом Vector")
        return self.length() < other.length()

    def __eq__(self, other):
        """ Порівнює вектори за довжиною (рівні) """
        if not isinstance(other, Vector):
            raise TypeError("Порівняння можливе лише з іншим об'єктом Vector")
        return self.length() == other.length()

    def __repr__(self):
        """ Представлення об'єкта """
        return f"Vector({self.x}, {self.y}, {self.z})"


# Приклади використання:
# Створення об'єктів vector1 та vector2
vector1 = Vector(1, 2, 3)
vector2 = Vector(4, 5, 6)

# Вивід результатів дії з класом в консоль
print(f"Введені дані: \nвектор 1 = {vector1}\nвектор 2 = {vector2}")
print("\n--- Математичні операції  з векторами ---")
print(f"Додавання двох векторів: {vector1 + vector2}")
print(f"Віднімання двох векторів: {vector1 - vector2}")
print(f"Множення першого вектору на число: {vector1 * 5}")
print(f"Множення другого вектору на число: {vector2 * 4}")
print("\n--- Порівняння векторів за довжиною ---")
print(f"Чи довжина вектору 1 < довжини вектору 2?: {vector1 < vector2}")
print(f"Чи довжина вектору 1 = довжині вектору 2?: {vector1 == vector2}")
print("\n--- Визначення довжини обох векторів ---")
print(f"Довжина вектору 1: {vector1.length()}")
print(f"Довжина вектору 2: {vector2.length()}")
