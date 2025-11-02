class CoffeeDrink:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def prepare(self):
        return f"Готовим базовый напиток {self.name}"
    
    def calculate_serving_time(self):
        return 3
    
    def get_description(self):
        return f"Напиток {self.name} - {self.price} руб."

class Espresso(CoffeeDrink):
    def prepare(self):
        return f"🍩 Варим эспрессо {self.name} под давлением 9 бар"
    
    def calculate_serving_time(self):
        return 2
    
    def get_description(self):
        return f"Крепкий эспрессо {self.name} - {self.price} руб."

class Latte(CoffeeDrink):
    def prepare(self):
        return f"🥛 Готовим латте {self.name} с молочной пенкой"
    
    def calculate_serving_time(self):
        return 4
    
    def get_description(self):
        return f"Нежный латте {self.name} - {self.price} руб."

class ColdBrew(CoffeeDrink):
    def prepare(self):
        return f"🧊 Подаем колд брю {self.name} со льдом"
    
    def calculate_serving_time(self):
        return 1
    
    def get_description(self):
        return f"Освежающий колд брю {self.name} - {self.price} руб."

class TurkishCoffee(CoffeeDrink):
    def prepare(self):
        return f"🔥 Варим турецкий кофе {self.name} в джезве"
    
    def calculate_serving_time(self):
        return 6
    
    def get_description(self):
        return f"Ароматный турецкий кофе {self.name} - {self.price} руб."

def process_coffee_drink(drink):
    print("=" * 40)
    print(drink.get_description())
    print(drink.prepare())
    print(f"Время приготовления: {drink.calculate_serving_time()} мин")
    print(f"Общее время с учетом подачи: {drink.calculate_serving_time() + 1} мин")

def create_coffee_bar(drinks):
    print("🏪 КОФЕЙНАЯ СТОЙКА - ПРОЦЕСС ПРИГОТОВЛЕНИЯ")
    total_time = 0
    for drink in drinks:
        process_coffee_drink(drink)
        total_time += drink.calculate_serving_time()
    print("=" * 40)
    print(f"Общее время приготовления всех напитков: {total_time} мин")

def demonstrate_polymorphism():
    drinks = [
        Espresso("Ристретто", 200),
        Latte("Ванильный латте", 280),
        ColdBrew("Айс кофе", 320),
        TurkishCoffee("По-восточному", 180),
        Espresso("Доппио", 220),
        Latte("Карамельный латте", 300)
    ]
    
    create_coffee_bar(drinks)
    
    print("\n🎯 ДЕМОНСТРАЦИЯ ПОЛИМОРФИЗМА В ДЕЙСТВИИ")
    
    coffee_list = [
        CoffeeDrink("Базовый кофе", 150),
        Espresso("Эспрессо маккиато", 230),
        Latte("Кокосовый латте", 290),
        ColdBrew("Нитро кофе", 350)
    ]
    
    print("\nРазные типы кофе в одном списке:")
    for coffee in coffee_list:
        print(f"- {coffee.prepare()}")
    
    print("\nСравнение времени приготовления:")
    for coffee in coffee_list:
        time = coffee.calculate_serving_time()
        print(f"- {coffee.name}: {time} мин {'⚡' if time < 3 else '⏳'}")

class CoffeeMachine:
    def make_drink(self, coffee_drink):
        print(f"\n☕ КОФЕМАШИНА: {coffee_drink.prepare()}")
        print(f"⏱️  Прогноз: {coffee_drink.calculate_serving_time()} мин")

print("🚀 ЗАПУСК ПРОГРАММЫ С ПОЛИМОРФИЗМОМ")
demonstrate_polymorphism()

print("\n🤖 РАБОТА С КОФЕМАШИНОЙ")
machine = CoffeeMachine()
machine.make_drink(Espresso("Эспрессо", 200))
machine.make_drink(Latte("Латте", 280))
machine.make_drink(ColdBrew("Колд брю", 320))
