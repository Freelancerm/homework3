class MyCollection:
    def __init__(self, data):
        # Зберігаємо дані як приватний атрибут
        self._data = data

    def __len__(self):
        """
        Реалізуємо власну логіку для отримання довжини.
        Рахуємо кількість елементів у списку
        """
        count = 0
        for _ in self._data:
            count += 1
        return count

    def __iter__(self):
        """ Робимо об'єкт ітерованим """
        return iter(self._data)

    def __getitem__(self, index):
        """ Дозволяємо доступ до елементів за індексом """
        return self._data[index]

    def __repr__(self):
        return f"MyCollection ({self._data})"


def my_len(collection):
    """
    Реалізація власної функції len().
    Використовує магічний метод __len__ об'єкта.
    """
    if hasattr(collection, '__len__'):
        return collection.__len__()
    raise TypeError(f"Заданий тип об'єкту '{type(collection)}' не має len()")


def my_sum(collection):
    """
    Реалізація власної функції sum()/
    Використовує ітерацію для об'єкта.
    """
    total = 0
    for item in collection:
        total += item
    return total


def my_min(collection):
    """
    Реалізація власної функції min().
    Перебирає елементи, щоб знайти найменший.
    """
    if not collection:
        raise ValueError("my_min() аргумент має пусте поле")

    min_value = collection[0]
    for item in collection:
        if item < min_value:
            min_value = item
    return min_value


# Створення тестового об'єкта
data_list = [10, 20, 5, 30, 15]
my_obj = MyCollection(data_list)

print(f"Заданий об'єкт: {my_obj}")

# Тест для написаних функцій та перевірка функціоалу в порівнянні з вбудованими
# Тест для my_len()
print("\n--- Тест my_len() ---")
print(f"Кількість значень(довжина) заданого об'єкту: {my_len(my_obj)}")
print(f"Використання вбудованої len(), для порівняння: {len(data_list)}")
if my_len(my_obj) == len(data_list):
    print("Тест пройшов успішно!")
else:
    print("Тест не складено, результат вбудованої функції відрізняється від результату власної")

# Тест для my_sum()
print("\n--- Тест my_sum() ---")
print(f"Сума елементів об'єкту: {my_sum(my_obj)}")
print(f"Використання вбудованої sum(), для порівняння: {sum(data_list)}")
if my_sum(my_obj) == sum(data_list):
    print("Тест пройшов успішно!")
else:
    print("Тест не складено, результат вбудованої функції відрізняється від результату власної")

# Тест для my_min()
print("\n--- Тест my_min() ---")
print(f"Мінімальний елемент об'єкту: {my_min(my_obj)}")
print(f"Використання вбудованої min(), для порівняння: {min(data_list)}")
if my_min(my_obj) == min(data_list):
    print("Тест пройшов успішно!")
else:
    print("Тест не складено, результат вбудованої функції відрізняється від результату власної")
