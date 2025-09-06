class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        """ Порівнює, чи вік поточної людини менший за вік іншої. """
        return self.age < other.age

    def __eq__(self, other):
        """ Порівнює чи вік поточної людини віку іншої """
        return self.age == other.age

    def __gt__(self, other):
        """ Порівнює чи вік поточної людини більший за вік іншої """
        return self.age > other.age

    def __repr__(self):
        """ Допоміжний метод для зручного виведення результату в консоль """
        return f"{self.name}, вік: {self.age} "


# Створення програми для сортування списку за віком
# Створення списку об'єктів
people = [
    Person("Владислав", 20),
    Person("Ольга", 21),
    Person("Олександр", 44),
    Person("Марія", 33),
    Person("Петро", 20),
]

print(f"Список людей до сортування:\n{people}")
# Сортування списку
print(f"Список людей після сортування за віком:\n{sorted(people)}")
