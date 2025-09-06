import re


class User:
    def __init__(self, first_name, last_name, email):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email

    @property
    def first_name(self):
        """ Отримує ім'я користувача """
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        """ Встановлює ім'я користувача """
        self.__first_name = value

    @property
    def last_name(self):
        """ Отримує прізвище користувача """
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        """ Встановлює прізвище користувача """
        self.__last_name = value

    @property
    def email(self):
        """ Отримує електронну пошту користувача """
        return self.__email

    @email.setter
    def email(self, value):
        """ Встановлює електронну пошту користувача """
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        """ Перевірка формату email - адреси """
        if not re.match(email_regex, value):
            raise TypeError("Невірний формат e-mail адреси 'example@domain.com'")
        self.__email = value


# Задаємо користувача
user1 = User("Volodymyr", "Holoborodjko", "volodya.holobod@gmail.com")

# Перевірка класу та методів
print(f"Користувач: {user1.first_name} {user1.last_name}")
print(f"Email: {user1.email}")
print(f"\nСпроба змінити email у вірному форматі")
user1.email = "holoborodjko@edu.ua"
print(f"Новий email: {user1.email}")
print(f"\nСпроба змінити email на не підтримуючий формат (отримуємо помилку)")
user1.email = "holobod.com"
