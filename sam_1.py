class CoffeeDrink:
    def __init__(self, name, coffee_type, size, temperature, price, rating=0):
        self.name = name
        self.coffee_type = coffee_type
        self.size = size
        self.temperature = temperature
        self.price = price
        self.rating = rating
        self.is_available = True
    
    def display_info(self):
        status = "доступен" if self.is_available else "не доступен"
        print(f"🍩 Напиток: {self.name}")
        print(f"   Тип: {self.coffee_type}")
        print(f"   Размер: {self.size}")
        print(f"   Температура: {self.temperature}")
        print(f"   Цена: {self.price} руб.")
        print(f"   Рейтинг: {'★' * self.rating}{'☆' * (5 - self.rating)} ({self.rating}/5)")
        print(f"   Статус: {status}")
    
    def rate_drink(self, new_rating):
        if 0 <= new_rating <= 5:
            self.rating = new_rating
            print(f"Рейтинг напитка '{self.name}' обновлен: {new_rating}/5")
        else:
            print("Рейтинг должен быть от 0 до 5")
    
    def change_price(self, new_price):
        old_price = self.price
        self.price = new_price
        print(f"Цена напитка '{self.name}' изменена: {old_price} → {new_price} руб.")
    
    def toggle_availability(self):
        self.is_available = not self.is_available
        status = "доступен" if self.is_available else "не доступен"
        print(f"Статус напитка '{self.name}' изменен: {status}")
    
    def calculate_discount_price(self, discount_percent):
        discount_amount = self.price * discount_percent / 100
        final_price = self.price - discount_amount
        return final_price

latte = CoffeeDrink("Латте классический", "кофе с молоком", "средний", "горячий", 250, 4)
cold_brew = CoffeeDrink("Колд брю", "холодный кофе", "большой", "холодный", 300, 5)
espresso = CoffeeDrink("Эспрессо", "черный кофе", "маленький", "горячий", 150, 3)

print("=== КОФЕЙНАЯ КАРТА ===\n")

latte.display_info()
print()
cold_brew.display_info()
print()
espresso.display_info()

print("\n=== ДЕЙСТВИЯ С НАПИТКАМИ ===")

latte.rate_drink(5)
print()

espresso.change_price(180)
print()

discount = 20
discounted_price = cold_brew.calculate_discount_price(discount)
print(f"Цена '{cold_brew.name}' со скидкой {discount}%: {discounted_price:.0f} руб.")
print()

latte.toggle_availability()
print()

print("\n=== ОБНОВЛЕННАЯ КОФЕЙНАЯ КАРТА ===")
latte.display_info()
