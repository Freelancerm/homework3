class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        """
        Додавання двох дробових чисел.
        Для додавання, дробові число приводяться до спільного знаменника.
        """
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        """
        Віднімання дробових чисел.
        Дробові числа приводяться до спільного знаменника, а потім чисельники віднімаються.
        """
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        """
        Множення двох дробових чисел.
        Чисельник одного дробу множиться на чисельник іншого, а знаменник на знаменник відповідно.
        """
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        """
        Метод ділення дробових чисел.
        Ділення реалізується як множення на обернений дріб.
        """
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __repr__(self):
        """
        Метод для представлення об'єкта у вигляді рядка.
        В читабельному форматі, наприклад "1/2".
        :return:
        """
        return f"{self.numerator}/{self.denominator}"


# Приклад використання
fraction1 = Fraction(1, 2)
fraction2 = Fraction(1, 4)

print(f"Введені дані: \nдріб 1 = {fraction1}\nдріб 2 = {fraction2}")
print("\n--- Математичні операції  з дробовими числами ---")
print(f"Додавання двох дробів: {fraction1 + fraction2}")
print(f"Віднімання двох дробів: {fraction1 - fraction2}")
print(f"Множення двох дробів: {fraction1 * fraction2}")
print(f"Ділення двох дробів: {fraction1 / fraction2}")
