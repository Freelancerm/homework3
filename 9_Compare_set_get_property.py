class ProductWithGetSet:
    def __init__(self, name, price):
        self.name = name
        self.__price = 0 # Ініціалізація для уникнення помилок
        self.set_price(price)

    def get_price(self):
        """ Повертає ціну товару """
        return self.__price

    def set_price(self, new_price):
        """ Встановлює нову ціну товару з перевіркою на від'ємне значення """
        if new_price < 0:
            raise ValueError("Ціна не може бути від'ємною!")
        self.__price = new_price


class ProductWithProperty:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        """ Геттер для ціни """
        return self._price

    @price.setter
    def price(self, new_price):
        """ Сеттер для ціни з перевіркою """
        if new_price < 0:
            raise ValueError("Неможливо щоб ціна була від'ємною!")
        self._price = new_price


class PriceWithDescriptor:
    """ Дескриптор, що перевіряє значення ціни """

    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.private_name)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Від'ємна ціна! Це не припустимо")
        instance.__dict__[self.private_name] = value


class ProductWithDescriptor:
    price = PriceWithDescriptor()

    def __init__(self, name, price):
        self.name = name
        self.price = price


def test_product_class(product_class, name, initial_price, new_price):
    """
    Тестова програма (функція), яка створює об'єкти кожного щ цих класів та намагається:
        Отримати та змінити ціну товару.
        Встановити від'ємне значення ціни та впевнитись, що воно правильно обробляється (викидання ValueError)
    """
    print(f"--- Тестування {product_class.__name__} ---")

    # Створення об'єкта
    try:
        test_product = product_class(name, initial_price)
        print(f"Створено {test_product.name} з ціною {initial_price:.2f} грн.")

        # Отримання початкової ціни
        if hasattr(test_product, 'get_price'):
            print(f"Початкова ціна: {test_product.get_price():.2f} грн.")
        else:
            print(f"Початкова ціна: {test_product.price:.2f} грн.")

        # Зміна ціни
        print(f"Спроба змінити ціну на {new_price:.2f} грн.....")
        if hasattr(test_product, 'get_price'):
            test_product.set_price(new_price)
        else:
            test_product.price = new_price

        # Отримання нової (зміненої) ціни
        if hasattr(test_product, 'get_price'):
            print(f"Нова ціна: {test_product.get_price():.2f} грн.")
        else:
            print(f"Нова ціна: {test_product.price:.2f} грн.")

    except Exception as ex:
        print(f"Помилка при створенні або зміні: {ex}")
        # Заглушка для уникнення наступних помилок
        test_product = None

    # Тест з від'ємною ціною, при умові що об'єкт було успішно створено
    if test_product is not None:
        print("Спроба встановити від'ємну ціну....")
        try:
            if hasattr(test_product, 'set_price'):
                test_product.set_price(-111)
            else:
                test_product.price = -111
        except ValueError as ex:
            print(f"Успішно перехоплено помилку: {ex}")
        except Exception as ex:
            print(f"Неочікувана помилка при встановленні від'ємної ціни: {ex}")
    else:
        print("Тест з від'ємною ціною пропущено через попередню помилку.")

    print("-" * 30)


"""
Завдання 3.
    Порівняння підходів:
    
        Сеттери/Геттери:
            Метод, який використовує явні методи get_price() а set_price() для доступу до атрибутів.
            Переваги:
                Явно показує внутрішню логіку при доступі до атрибута
            Недоліки:
                Багатослівний та громіздкий синтаксис, менш читабельний код. Наприклад:
                    Замість спрощеного product.price = 50 , доводиться писати product.set_price(50).
        Дескриптори:
            Окремі класи, які контролюють доступ до атрибутів. Потужний та гнучкий механізм, який дозволяє повторно використовувати логіку атрибутів між різними класами.
            Переваги:
                Гнучкість та можливість повторного використання коду. Ідеально підходить якщо є багато класів з однаковими вимогами до валідації (ціна,кількість,рейтинг і т.д.), 
                дає можливість використовувати один дескриптор для всіх.
            Недоліки:
                Для простої або 'одноразової' валідації ціни використовувати окремий клас-дескриптор - це надмірне рішення.
        Декоратор @property:
            Як на мене один з самих зрозумілих та маломістких способів для управління доступом до атрибутів. Він дозволяє використовувати звичайний синтаксис атрибутів,
            але за лаштунками виконується певна (своя) логіка.
            Переваги:
                Читабельність: Чистий та інтуітивно зрозумілий код. Звернення до атрибута як до звичайної змінної (product.price), а не як до результату виклику функції (product.get_price()).
                Гнучкість: Дозволяє почати з простого публічного атрибута, а потім, у разі потреби, додавати логіку перевірки або обчислення, не змінюючи зовнішній код, який використовує цей атрибут.
            Недоліки:
                Логіка валідації прив'язана до класу, що робить її менш придатною для повторного використання у великих проектах з багатьма ідентичними атрибутами.
           
Висновок: @property є найкращим вибором у нашому випадку. Для простого класу Product з одним або двома атрибутами, які потребують валідації, декоратор @property пропонує
          ідеальний баланс між читабельністю, простотою та ефейтивністю у застосуванні. Легка та елегантна інкапсуляція логіки валідації в середині класу, не ускладнюючи
          синтаксис для користувача.    
"""


class PriceUAH(PriceWithDescriptor):
    """ Дескриптор для ціни у гривнях, що зберігає значення. """
    pass


class CurrencyConverterDescriptor:
    """ Дескриптор для конвертації ціни в долари або євро """

    def __init__(self, currency_name, conversion_rate):
        self.currency_name = currency_name
        self.conversion_rate = conversion_rate

    def __get__(self, instance, owner):
        if instance is None:
            return self
        base_price_uah = instance.price_uah
        return f"{base_price_uah / self.conversion_rate:.2f} {self.currency_name}"

    def __set__(self, instance, value):
        raise AttributeError(f"Неможливо встановити конвертовану ціну безпосередньо в {self.currency_name}. Змініть базову ціну в UAH.")


class ProductWithCurrencyDescriptor:
    # Базова ціна зберігається в гривнях
    price_uah = PriceUAH()
    # Конвертування цін за допомогою дескриптора
    price_usd = CurrencyConverterDescriptor("usd", 40.50)  # Умовний курс, 1 USD = 40.50 UAH
    price_eur = CurrencyConverterDescriptor("eur", 44.00)  # Умовний курс, 1 EUR = 40.50 UAH

    def __init__(self, name, price_uah):
        self.name = name
        self.price_uah = price_uah


# Тести трьох класів
test_product_class(ProductWithGetSet, "Книга", 150.0, 180.5)
test_product_class(ProductWithProperty, "Системний блок", 25500.0, 23660.0)
test_product_class(ProductWithDescriptor, "Клавіатура", 750.0, 800.0)

# Тест конвертації валют
print("--- Тестування дескриптора з конвертацією валют ---")
product = ProductWithCurrencyDescriptor("Ноутбук", 56760)

print(f"Назва товару: {product.name}")
print(f"Ціна в UAH: {product.price_uah:.2f} грн")
print(f"Ціна в USD: {product.price_usd}")
print(f"Ціна в EUR: {product.price_eur}")

try:
    product.price_usd = 1000
except AttributeError as exc:
    print(f"Невдала спроба встановити ціну в долларах: {exc}")