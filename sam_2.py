class CoffeeDrink:
    def __init__(self, name, price, size="средний"):
        self.name = name
        self.price = price
        self.size = size
        self.is_available = True
        self.brew_strength = "средняя"
        self.milk_type = None
        self.sweetness_level = 0
        self.customizations = []

    def display_info(self):
        status = "доступен" if self.is_available else "не доступен"
        milk_info = f", молоко: {self.milk_type}" if self.milk_type else ""
        sweetness = "без сахара" if self.sweetness_level == 0 else f"сахар: {self.sweetness_level}/10"
        print(f"☕ {self.name} - {self.price} руб. ({self.size})")
        print(f"   Крепость: {self.brew_strength}, {sweetness}{milk_info}")
        print(f"   Статус: {status}")

    def apply_discount(self, percent):
        new_price = self.price * (100 - percent) / 100
        print(f"Скидка {percent}%: {self.price} → {new_price:.0f} руб.")
        return new_price

    def set_brew_strength(self, strength):
        strengths = ["слабая", "средняя", "крепкая", "очень крепкая"]
        if strength in strengths:
            self.brew_strength = strength
            print(f"Крепость {self.name} установлена: {strength}")
        else:
            print("Доступные крепости: слабая, средняя, крепкая, очень крепкая")

    def add_milk(self, milk_type):
        self.milk_type = milk_type
        print(f"Добавлено молоко: {milk_type}")

    def set_sweetness(self, level):
        if 0 <= level <= 10:
            self.sweetness_level = level
            print(f"Уровень сладости установлен: {level}/10")
        else:
            print("Уровень сладости должен быть от 0 до 10")

    def add_customization(self, customization):
        self.customizations.append(customization)
        print(f"Добавлена опция: {customization}")

    def show_customizations(self):
        if self.customizations:
            print(f"Дополнения для {self.name}:")
            for item in self.customizations:
                print(f"   - {item}")
        else:
            print(f"У {self.name} нет дополнительных опций")

    def calculate_brew_time(self):
        times = {"слабая": 2, "средняя": 3, "крепкая": 4, "очень крепкая": 5}
        base_time = times.get(self.brew_strength, 3)
        if self.milk_type:
            base_time += 1
        return base_time


latte = CoffeeDrink("Латте", 250)
espresso = CoffeeDrink("Эспрессо", 150, "маленький")
cappuccino = CoffeeDrink("Капучино", 280, "большой")

print("=== БАЗОВАЯ ИНФОРМАЦИЯ ===")
latte.display_info()
print()
espresso.display_info()

print("\n=== НАСТРОЙКА НАПИТКОВ ===")
latte.set_brew_strength("крепкая")
latte.add_milk("овсяное")
latte.set_sweetness(3)
latte.add_customization("корица")
latte.add_customization("тертый шоколад")

print()
espresso.set_brew_strength("очень крепкая")
espresso.set_sweetness(0)

print()
cappuccino.add_milk("кокосовое")
cappuccino.set_sweetness(7)
cappuccino.add_customization("ванильный сироп")

print("\n=== ИТОГОВАЯ ИНФОРМАЦИЯ ===")
latte.display_info()
print()
espresso.display_info()
print()
cappuccino.display_info()

print("\n=== ДОПОЛНИТЕЛЬНЫЕ ОПЦИИ ===")
latte.show_customizations()
cappuccino.show_customizations()

print("\n=== ВРЕМЯ ПРИГОТОВЛЕНИЯ ===")
print(f"Время приготовления латте: {latte.calculate_brew_time()} мин")
print(f"Время приготовления эспрессо: {espresso.calculate_brew_time()} мин")
print(f"Время приготовления капучино: {cappuccino.calculate_brew_time()} мин")

print("\n=== АКЦИИ ===")
latte.apply_discount(20)
