class BinaryNumber:
    def __init__(self, value):
        """ Ініціалізує двійкове число з десяткового значення. """
        if not isinstance(value, int):
            raise TypeError("Значення має бути цілим числом")
        self.value = value

    def __and__(self, other):
        """"
        Метод для операції AND.
        Виконує побітове 'I' між двома двійковими числами
        """
        return BinaryNumber(self.value & other.value)

    def __or__(self, other):
        """
        Метод для операції OR.
        Виконує побітове 'АБО' між двома двійковими числами
        """
        return BinaryNumber(self.value | other.value)

    def __xor__(self, other):
        """
        Метод для операції XOR.
        Виконує побітове 'ВИКЛЮЧНЕ АБО' між двома двійковими числами
        """
        return BinaryNumber(self.value ^ other.value)

    def __invert__(self):
        """
        Метод для операції NOT.
        Виконує побітове 'НЕ', інвертуючи всі біти.
        """
        return BinaryNumber(~self.value)

    def __repr__(self):
        """
        Представлення об'єкта для виведення об'єкта в консоль.
        Вивід у вигляді десяткового та двійкового значення для зручності.
        """
        return f"Бінарне число:(десяткове={self.value}, двійкове={bin(self.value)})"


# Приклад використання:
# Створення об'єктів BinaryNumber
num1 = BinaryNumber(10)
num2 = BinaryNumber(20)

#Вивід результату взаємодії з класом в консоль
print(f"--- Введені значення ---")
print(f"Перше {num1} \nДруге {num2}")
print("\n--- Демонстрація побітових операцій ---")
print(f"Результат AND: {num1 & num2}")
print(f"Результат OR: {num1 | num2}")
print(f"Результат XOR: {num1 ^ num2}")
print(f"Результат NOT(від першого числа): {~num1}")
print(f"Результат NOT(від другого числа): {~num2}")