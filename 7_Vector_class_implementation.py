import math


class Vector:
    def __init__(self, *components):
        """ Ініціалізує вектор з довільною кількістю чисел """
        if not all(isinstance(c, (int, float)) for c in components):
            raise TypeError("Всі компоненти вектора повинні бути числами (int або float)")
        self._components = components

    def __repr__(self):
        """ Представлення об'єкта в читабельному вигляді """
        return f"Вектор ({', '.join(map(str, self._components))})"

    def length(self):
        """ Обчислює довжину вектора """
        return round(math.sqrt(sum(c ** 2 for c in self._components)), 2)

    def __add__(self, other):
        """ Додає два вектори між собою. """
        if not isinstance(other, Vector) or len(self._components) != len(other._components):
            raise ValueError("Вектори мають бути однакового розміру для додавання.")
        new_components = [c1 + c2 for c1, c2 in zip(self._components, other._components)]
        return Vector(*new_components)

    def __sub__(self, other):
        """ Віднімає один вектор від іншого. """
        if not isinstance(other, Vector) or len(self._components) != len(other._components):
            raise ValueError("Вектори мають бути однакового розміру для віднімання.")
        new_components = [c1 - c2 for c1, c2 in zip(self._components, other._components)]
        return Vector(*new_components)

    def __mul__(self, other):
        """ Обчислює скалярний добуток """
        if isinstance(other, Vector):
            if len(self._components) != len(other._components):
                raise ValueError("Вектори мають бути однакового розміру для скалярного добутку.")
            return sum(c1 * c2 for c1, c2 in zip(self._components, other._components))
        return NotImplemented

    def __eq__(self, other):
        """ Перевіряє, чи рівні довжини векторів """
        if not isinstance(other, Vector):
            return NotImplemented
        return self.length() == other.length()

    def __lt__(self, other):
        """ Перевіряє, чи довжина поточного вектора менша за довжину іншого.  """
        if not isinstance(other, Vector):
            return NotImplemented
        return self.length() < other.length()

    def __gt__(self, other):
        """ Перевіряє, чи поточна довжина вектора більша за довжину іншого """
        if not isinstance(other, Vector):
            return NotImplemented
        return self.length() > other.length()


# Створення об'єктів
v1 = Vector(3, 4, 22, 35)
v2 = Vector(5, 12, 33, 42)

# Приклад використання методів класу
print(f"Вектор1 = {v1}. \nВектор2 = {v2}")
print("--- Математичні операції з векторами ---")
print(f"Результат додавання двох векторів = {v1 + v2}")
print(f"Результат віднімання двох векторів = {v1 - v2}")
print(f"Результат обчислення скалярного добутку двох векторів = {v1 * v2}")
print("\n--- Порівняння довжин векторів 1 та 2 ---")
print(f"Довжина вектору 1 = {v1.length()} \nДовжина вектору 2 = {v2.length()}")
print(f"Довжина вектору 1 = довжині вектору 2 : {v1 == v2}")
print(f"Довжина вектору 1 > довжини вектору 2 : {v1 > v2}")
print(f"Довжина вектору 1 < довжини вектору 2 : {v1 < v2}")
