class Price:
    def __init__(self, _value):
        """
        Метод ініціалізації.
        """
        if not isinstance(_value, (int, float)):
            raise TypeError("Ціна повинна бути числом int або float.")
        # Зберігаємо ціну з точністю до двох десяткових знаків
        self._value = round(float(_value), 2)
        
    def __repr__(self):
        """ Повернення даних про ціну у сприятливому форматі та додавання валюти (грн) """
        return f"Ціна {self._value:.2f} грн."
    
    def __add__(self, other):
        """ Операції з додаванням цін між собою """
        if isinstance(other, Price):
            return Price(self._value + other._value)
        elif isinstance(other, (int, float)):
            return Price(self._value + other)
        return NotImplemented
    
    def __sub__ (self, other):
        """ Операції з відніманням цін між собою """
        if isinstance(other, Price):
            return Price(self._value - other._value)
        elif isinstance(other, (int, float)):
            return Price(self._value - other)
        return NotImplemented
    
    def __eq__(self, other):
        """ Чи рівні ціни між собою """
        if isinstance(other, Price):
            return self._value == other._value
        return NotImplemented

    def __lt__(self, other):
        """ Чи перша ціна менша за другу ціну """
        if isinstance(other, Price):
            return self._value < other._value
        return NotImplemented

    def __gt__(self, other):
        """ Чи перша ціна більша за другу ціну """
        if isinstance(other, Price):
            return self._value > other._value
        return NotImplemented

    @property
    def value(self):
        """
        Повертає значення ціни.
        Дозволяє доступ до _value як до властивості (price.value).
        """
        return self._value


# Застосування у класі PaymentGateway
class PaymentGateway:
    def process_payment(self, amount: Price, card_info: str):
        print(f"Початок обробки платежу на суму {amount}...")

        if amount.value <= 0:
            print("Помилка: Неприпустима сума для платежу.")
            return False

        if self._connect_to_payment_system(amount, card_info):
            print("Платіж успішно оброблено.")
            return True
        else:
            print("Помилка при обробці платежу.")
            return False

    @staticmethod
    def _connect_to_payment_system(amount: Price, card_info: str):
        print(f"З'єднання з платіжним сервісом для списання {amount} з картки {card_info}.")
        return True


# Приклад використання класу Price
p1 = Price(99.99)
p2 = Price(50.2)
p3 = Price(23)

print(f"Ціна 1: {p1}\nЦіна 2: {p2}\nЦіна 3: {p3}\n")
print("--- Додавання та віднімання ---")
print(f"Сума цін: {p1 + p2 + p3}")
print(f"Різниця цін: {p1 - p2 - p3}")
print("\n--- Операції порівняння ---")
print(f"Чи більша перша ціна за другу ціну?: {p1 > p2}")
print(f"Чи перша та третя ціна рівні?: {p1 == p3}")

# Сценарій використання PaymentGateway
# Створюємо об'єкт PaymentGateway
payment_processor = PaymentGateway()

# Викликаємо метод для обробки платежу
print("\n--- Сценарій 1: Успішна оплата ---")
card_details = "4444-5555-6666-7777"
is_successful = payment_processor.process_payment(p1, card_details)

print(f"Статус транзакції: {'Успішна' if is_successful else 'Невдала'}")

print("\n--- Сценарій 2: Невдала оплата (неприпустима сума) ---")
# Створюємо Price з недопустимим значенням (наприклад, 0)
invalid_price = p3 - p1
is_successful = payment_processor.process_payment(invalid_price, "...")

print(f"Статус транзакції: {'Успішна' if is_successful else 'Невдала'}")
