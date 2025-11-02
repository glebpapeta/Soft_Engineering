class CoffeeDrink:
    def __init__(self, name, price, size="средний"):
        self._name = name
        self._price = price
        self._size = size
        self._is_available = True
        self._brew_strength = "средняя"
        self.__secret_recipe = "базовый рецепт"
        self.__sales_count = 0

    def display_info(self):
        status = "доступен" if self._is_available else "не доступен"
        print(f"☕ {self._name} - {self._price} руб. ({self._size})")
        print(f"   Крепость: {self._brew_strength}")
        print(f"   Статус: {status}")

    def get_name(self):
        return self._name

    def set_price(self, new_price):
        if new_price > 0:
            self._price = new_price
            print(f"Цена изменена на {new_price} руб.")
        else:
            print("Цена должна быть положительной")

    def get_price(self):
        return self._price

    def _change_availability(self, available):
        self._is_available = available
        status = "доступен" if available else "не доступен"
        print(f"Статус изменен: {status}")

    def make_available(self):
        self._change_availability(True)

    def make_unavailable(self):
        self._change_availability(False)

    def __prepare_ingredients(self):
        print(f"Подготавливаются ингредиенты для {self._name}...")

    def __calculate_brew_time(self):
        times = {"слабая": 2, "средняя": 3, "крепкая": 4}
        return times.get(self._brew_strength, 3)

    def prepare_drink(self):
        self.__prepare_ingredients()
        brew_time = self.__calculate_brew_time()
        print(f"Напиток готовится {brew_time} минуты...")
        self.__increment_sales()
        print(f"✅ {self._name} готов!")

    def __increment_sales(self):
        self.__sales_count += 1

    def get_sales_count(self):
        return self.__sales_count

    def _get_secret_recipe(self):
        return f"Секретный рецепт {self._name}: {self.__secret_recipe}"

    def set_brew_strength(self, strength):
        if strength in ["слабая", "средняя", "крепкая"]:
            self._brew_strength = strength
            print(f"Крепость установлена: {strength}")
        else:
            print("Недопустимая крепость")


class PremiumCoffee(CoffeeDrink):
    def __init__(self, name, price, size="средний", origin="Эфиопия"):
        super().__init__(name, price, size)
        self._origin = origin
        self.__aging_months = 12

    def display_info(self):
        super().display_info()
        print(f"   Происхождение: {self._origin}")

    def get_aging_info(self):
        return f"Выдержка: {self.__aging_months} месяцев"

    def _premium_preparation(self):
        print(f"Особая подготовка премиум кофе из {self._origin}")


print("=== БАЗОВЫЙ КЛАСС ===")
latte = CoffeeDrink("Латте", 250)
latte.display_info()

print("\n=== ИНКАПСУЛЯЦИЯ: ГЕТТЕРЫ И СЕТТЕРЫ ===")
print(f"Название напитка: {latte.get_name()}")
print(f"Текущая цена: {latte.get_price()} руб.")
latte.set_price(280)
latte.set_price(-100)

print("\n=== ИНКАПСУЛЯЦИЯ: ДОСТУП К ПРИВАТНЫМ МЕТОДАМ ===")
latte.prepare_drink()
latte.prepare_drink()
print(f"Количество продаж: {latte.get_sales_count()}")

print("\n=== ИНКАПСУЛЯЦИЯ: ЗАЩИЩЕННЫЕ МЕТОДЫ ===")
latte.make_unavailable()
latte.display_info()
latte.make_available()

print("\n=== НАСЛЕДОВАНИЕ И ИНКАПСУЛЯЦИЯ ===")
premium = PremiumCoffee("Эфиопский Премиум", 500, "маленький", "Эфиопия Йиргачеффе")
premium.display_info()
print(premium.get_aging_info())

print("\n=== ПРОВЕРКА ДОСТУПА ===")
try:
    print(latte.__secret_recipe)
except AttributeError as e:
    print(f"Ошибка доступа к приватному атрибуту: {e}")

try:
    print(premium.__aging_months)
except AttributeError as e:
    print(f"Ошибка доступа к приватному атрибуту: {e}")

print("\n=== ИЗМЕНЕНИЕ СВОЙСТВ ===")
latte.set_brew_strength("крепкая")
latte.set_brew_strength("очень крепкая")
latte.display_info()
