class CoffeeDrink:
    def __init__(self, name, price, size="средний"):
        self.name = name
        self.price = price
        self.size = size
        self.is_available = True
        self.brew_strength = "средняя"
    
    def display_info(self):
        status = "доступен" if self.is_available else "не доступен"
        print(f"☕ {self.name} - {self.price} руб. ({self.size})")
        print(f"   Крепость: {self.brew_strength}")
        print(f"   Статус: {status}")
    
    def set_brew_strength(self, strength):
        self.brew_strength = strength
        print(f"Крепость {self.name} установлена: {strength}")

class HotCoffee(CoffeeDrink):
    def __init__(self, name, price, size="средний", temperature=85):
        super().__init__(name, price, size)
        self.temperature = temperature
        self.has_foam = False
    
    def add_foam(self):
        self.has_foam = True
        print(f"Добавлена молочная пенка в {self.name}")
    
    def display_info(self):
        super().display_info()
        foam_status = "с пенкой" if self.has_foam else "без пенки"
        print(f"   Температура: {self.temperature}°C, {foam_status}")

class IcedCoffee(CoffeeDrink):
    def __init__(self, name, price, size="большой", ice_amount="среднее"):
        super().__init__(name, price, size)
        self.ice_amount = ice_amount
        self.has_straw = True
    
    def add_syrup(self, syrup_type):
        print(f"Добавлен сироп '{syrup_type}' в {self.name}")
    
    def display_info(self):
        super().display_info()
        straw_status = "с трубочкой" if self.has_straw else "без трубочки"
        print(f"   Лед: {self.ice_amount}, {straw_status}")

print("=== ГОРЯЧИЕ НАПИТКИ ===")
latte = HotCoffee("Латте", 250, "большой", 75)
cappuccino = HotCoffee("Капучино", 280, "средний", 80)
latte.add_foam()
latte.display_info()
print()
cappuccino.display_info()

print("\n=== ХОЛОДНЫЕ НАПИТКИ ===")
iced_latte = IcedCoffee("Айс Латте", 300, "большой", "обильное")
cold_brew = IcedCoffee("Колд Брю", 320, "средний", "минимальное")
iced_latte.add_syrup("ванильный")
iced_latte.display_info()
print()
cold_brew.display_info()

print("\n=== ИЗМЕНЕНИЕ СВОЙСТВ ===")
latte.set_brew_strength("крепкая")
cold_brew.set_brew_strength("слабая")

print("\n=== ПРОВЕРКА ТИПОВ ===")
print(f"Латте является HotCoffee: {isinstance(latte, HotCoffee)}")
print(f"Айс Латте является IcedCoffee: {isinstance(iced_latte, IcedCoffee)}")
print(f"Все являются CoffeeDrink: {isinstance(latte, CoffeeDrink)}")
